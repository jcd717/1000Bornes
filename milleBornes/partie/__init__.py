from flask import Blueprint, render_template, g, url_for, redirect

from moteur import cartes
from moteur.classes import *
from milleBornes import (getFileNameFromObjectCarte, makeTransparentEmptyImageByHeight, 
                         getLargeurCarte, getHauteurCarte)


#from lorem_text import lorem

bp = Blueprint('partie', __name__)

@bp.route('/Game/<int:nbJoueurs>')
def game(nbJoueurs=4):
    if nbJoueurs not in (2,4):
        return redirect(url_for('home.home'))

    # #g['Etape25']='coucou'
    # for c in cartes:
    #     print
    # g.cartes=cartes
    g.titre="Partie à {} joueurs".format(nbJoueurs)
    g.main = [cartes[Etape25], cartes[Etape50],
              cartes[Etape75], cartes[Etape100], cartes[Etape200], cartes[Prioritaire], cartes[AsDuVolant], ]
    g.imageDefausseVide = makeTransparentEmptyImageByHeight()

    
    return render_template('partie/partie.j2', getFileNameFromObjectCarte=getFileNameFromObjectCarte)
