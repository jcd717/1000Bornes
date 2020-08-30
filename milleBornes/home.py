from flask import Blueprint, render_template, g, session

from .listeCartes import getTitle

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    g.listeCartes=getTitle()
    g.continuer=None
    if session.get('partie') and not session['partie'].isTerminated:
        g.continuer=session['partie'].nombreJoueurs

    return render_template('home.j2')

