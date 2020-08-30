from moteur import ( etapes, parades, attaques, bottes, cartes, getNombreTotalCartes, 
                     mapClassCarteConcerteToDictObjectsCarteConcrete)
from moteur.classes import *
from flask import Blueprint, render_template, g, url_for
from milleBornes import makeTransparentEmptyImageByHeight, resizeImage, getFileNameFromObjectCarte

#from lorem_text import lorem

bp = Blueprint('listeCartes', __name__)

# Calculs divers
# --------------

def getTitle():
    title = url_for('listeCartes.listeCartes')
    title = title.split('/')
    title = title[len(title)-1]
    title = title.replace('-', ' ')
    return title



def maxLen(typeCarte): # typeCarte est 1 des sous-classes contrète de Carte: Etape, Parade ...
    #mapping={Attaque: attaques, Parade: parades, Etape: etapes, Botte: bottes}
    res=0
    for c in mapClassCarteConcerteToDictObjectsCarteConcrete[typeCarte].values():
        res=max(res,len(c.nom))
    return res+1


class CarteSansNomSansNombre(PasDeCarte):
    def __init__(self):
        self._nom = ' '  # un espace associé au CSS white-space: pre; pour afficher une contenu vide qui prend la place d'un lettre
        self._nombre = ''


# liste de dict à mettre dans g pour faire la page sans aucune chaîne en dur -> variable: html
#     attribut id de <div>  affichage HTML        liste d'objets Carte du type dans l'ordre d'affichage
#  [ { nomId: 'attaques', nomHTML: "Attaques", cartes: [ obj(FeuRouge), obj(LimitationDeVitesse)]}, ... les autres types de cartes ]

_ordreCartes= {
    Attaque: (cartes[FeuRouge], cartes[LimitationDeVitesse], cartes[Accident], cartes[Creve], cartes[PanneEssence]),
    Parade: (cartes[FeuVert], cartes[FinDeLimitation], cartes[Reparation], cartes[RoueDeSecours], cartes[Essence]),
    Botte: (cartes[Prioritaire], CarteSansNomSansNombre(), cartes[AsDuVolant], cartes[Increvable], cartes[Citerne]),
    Etape: (cartes[Etape25], cartes[Etape50], cartes[Etape75], cartes[Etape100], cartes[Etape200]),
}

ordreCartes={}
for k in _ordreCartes.keys():
    l=[]
    #scale=0.4
    hauteur=45
    for v in _ordreCartes[k]:
        d = {'carte': v, 
             'image':  makeTransparentEmptyImageByHeight(hauteur) if isinstance(v,CarteSansNomSansNombre) else resizeImage(v,hauteur)  }
        l.append(d)
    ordreCartes.update({k: l})

del _ordreCartes,k,l,v,d, hauteur

ordreTypes=(Attaque, Parade, Botte, Etape)
nomTypes = {
    Attaque: {'nomId': 'attaques', 'nomHTML': "Attaques"},
    Parade: {'nomId': 'parades', 'nomHTML': "Parades"},
    Botte: {'nomId': 'bottes', 'nomHTML': "Bottes"},
    Etape: {'nomId': 'etapes', 'nomHTML': "Bornes"},
}

html=[]
for tc in ordreTypes:
    html.append({'nomId': nomTypes[tc]['nomId'],
                 'nomHTML': nomTypes[tc]['nomHTML'],
                 'cartes': ordreCartes[tc],
                 'maxLen': maxLen(tc),
    })

del ordreCartes, ordreTypes, nomTypes, tc




@bp.route('/Liste-des-cartes')
def listeCartes():    
    g.html=html
    #debug: getFileNameFromObjectCarte(html[0]['cartes'][0]['carte'])
    g.title = getTitle()
    g.total = getNombreTotalCartes()

    return render_template('listeCartes.j2', getFileNameFromObjectCarte=getFileNameFromObjectCarte)
