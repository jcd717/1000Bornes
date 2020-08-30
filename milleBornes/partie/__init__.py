from flask import Blueprint, render_template, g, url_for, redirect, session

#from moteur import cartes
#from moteur.classes import *
from moteur import Partie

from milleBornes import (getFileNameFromObjectCarte, makeTransparentEmptyImageByHeight, 
                         getLargeurCarte, getHauteurCarte)


#from lorem_text import lorem

bp = Blueprint('partie', __name__)



@bp.route('/Game/<int:nbJoueurs>')
def game(nbJoueurs=4):


    if nbJoueurs not in (2,4):
        return redirect(url_for('home.home'))

# vérifier le request parameter "continuer" et alors vérifier que la session n'a pas expirée (donc réduire sa durée pour le test)
    if not session.get('partie'):
        session['partie'] = Partie(nbJoueurs)
    elif not session['partie'].isTerminated:
        print('pas fini')

    g.titre = "Partie à {} joueurs".format(nbJoueurs)
    
    session['partie'].joueurs[0].cartesEnMain.cartes.append(session['partie'].tas.pop()) #MAUVAIS
    #->faire joueur.piocher()
    
    g.main = session['partie'].joueurs[0].cartesEnMain.cartes

    g.imageCarteVide = makeTransparentEmptyImageByHeight()

    
    return render_template('partie/partie.j2', getFileNameFromObjectCarte=getFileNameFromObjectCarte)
