from moteur import Prioritaire
import os,re
import markdown

from flask import Flask, request, send_from_directory, url_for

from flask_session import Session

from moteur import Carte



def create_app(test_config=None):

    ### TUYAUTERIE ###

    # create and configure the app
    # c'est la doc qui dit qu'il vaut mieux utiliser la forme split
    app = Flask(__name__.split('.')[0], instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        TOOLBAR=os.environ.get('TOOLBAR'),
        TITRE='1000 Bornes',
        DEBUG_TB_TEMPLATE_EDITOR_ENABLED=True,
        #EXPLAIN_TEMPLATE_LOADING=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # contient essentiellement la "SECRET_KEY"
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # si la variable d'environnement "SECRET_KEY" existe alors c'est la bonne (bonne pratique docker)
    if os.environ.get('SECRET_KEY'):
        app.config.from_mapping(SECRET_KEY=os.environ['SECRET_KEY'],)

    # autoescape sur .j2
    from jinja2 import select_autoescape

    app.jinja_env.autoescape = select_autoescape(
        default_for_string=True,
        disabled_extensions=('txt',),
        default=True
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # la toolbar
    if app.config['TOOLBAR']:
        from flask_debugtoolbar import DebugToolbarExtension
        #toolbar = DebugToolbarExtension(app)
        DebugToolbarExtension(app)
        print("TOOLBAR installée")
        if app.debug:  # lorsqu'il y a la toolbar, le logger n'envoie plus les debug
            app.logger.propagate = True


    @app.route('/robots.txt')
    @app.route('/humans.txt')
    @app.route('/favicon.ico')
    @app.route('/sitemap.xml')
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    # session côté serveur
    #redis = os.environ.get('REDIS') if os.environ.get('REDIS') else False
    app.config.update(
        #SESSION_TYPE='redis' if redis else 'filesystem',
        SESSION_TYPE='filesystem',
        SESSION_USE_SIGNER=True,
        SESSION_FILE_DIR=os.path.join(app.instance_path, 'flask_session'),
        PERMANENT_SESSION_LIFETIME=2 * 24 * 3600 + 3600  # 49 heures
    )
    # if redis:
    #     from redis import Redis
    #     hp = redis.split(':')
    #     h = hp[0]
    #     p = 6379 if len(hp) == 1 else int(hp[1])
    #     app.config['SESSION_REDIS'] = Redis(host=h, port=p)
    Session(app)

    

    ### Mon appli ###

    # from primes import primes
    # app.register_blueprint(primes.bp)
    # app.add_url_rule('/', endpoint='homepage')

    from . import listeCartes
    app.register_blueprint(listeCartes.bp)

    from . import home
    app.register_blueprint(home.bp)

    from . import regles
    app.register_blueprint(regles.bp)
    
    from .partie import bp  # partie est un package
    app.register_blueprint(bp)

    return app



def getFileNameFromObjectCarte(carte: Carte):
    return carte.__class__.__name__+'.jpg'


from PIL import Image
import base64
from io import BytesIO


# calcul de _largeurCarte et _hauteurCarte d'une carte
prioritaire = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'static/images/cartes/', getFileNameFromObjectCarte(Prioritaire()))
prioritaire = Image.open(prioritaire)
_largeurCarte, _hauteurCarte = prioritaire.size
prioritaire.close()
del prioritaire



def rescaleImage(image:Carte,scale:float=1):
    """ Retourne une chaîne base64 après 'rescale' de l'image """
    image = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static/images/cartes/',getFileNameFromObjectCarte(image))
    image=Image.open(image)
    w,h=image.size
    resizeImage=image.resize((int(w*scale),int(h*scale)))
    image.close()

    buffered = BytesIO()
    resizeImage.save(buffered, format="JPEG")
    resizeImage.close()
    return base64.b64encode(buffered.getvalue()).decode('ascii')

def resizeImage(image:Carte,hauteur:int):
    """ Alernative à rescaleImage() où on contraint la hauteur """
    scale = hauteur / _hauteurCarte
    return rescaleImage(image,scale)


def makeTransparentEmptyImage(scale=1):
    """ Retourne une chaîne base64 d'une image vide de Carte """
    image = Image.new("RGBA", (_largeurCarte,_hauteurCarte))
    resizeImage = image.resize((int(_largeurCarte*scale), int(_hauteurCarte*scale)))
    buffered = BytesIO()
    resizeImage.save(buffered, format="PNG")
    resizeImage.close()
    return base64.b64encode(buffered.getvalue()).decode('ascii')


def makeTransparentEmptyImageByHeight(hauteur:int):
    """ Alernative à makeTransparentEmptyImage() où on contraint la hauteur  """
    scale = hauteur / _hauteurCarte
    return makeTransparentEmptyImage(scale)


_reglesMD=None
def getReglesMD():
    global _reglesMD
    #_reglesMD=None # pour l'élaboration du MD, reparser à chaque fois
    if not _reglesMD:
        #print('CALCULS')
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'regles.md')
        with open(filename) as f:
            mdFile = f.read()

        _reglesMD=markdown.markdown(
            mdFile,
            extensions=['sane_lists', 'tables', 'toc', ],
            extension_configs={'toc': {'title': 'Table des matières','toc_depth': 2}},
        )
        # remplacer {{STATIC}} par l'URL qui défint le chemin /static
        repl=url_for('static',filename='style.css') # la valeur de filename n'a pas d'importance puisque le but est de le supprimer
        repl = os.path.dirname(repl)
        _reglesMD = re.sub(r'{{\s*STATIC\s*}}',repl,_reglesMD)


    return _reglesMD
