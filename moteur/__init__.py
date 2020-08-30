from .classes import Attaque,Parade,Botte,Etape,Speciale,Carte
from .partie import Partie


# "cartes": dictionnaire de toutes les cartes (objets concrets) 
# calculée à partir de la classe Carte (recherche des classes filles de 2ème niveau)
# d'autres dictionnaires par type de carte sont calculés
# l'objectif du moteur est de n'avoir qu'une instance de carte par classe concrète 
# (bien que j'utilse le singleton-decorator de Pypi) -> qui ne marche pas terrible, il faut toujours mettre .__wrapped__
# => je n'utilise plus
cartes, attaques, parades, bottes, etapes, speciales = {}, {}, {}, {}, {}, {}
mapClassCarteConcerteToDictObjectsCarteConcrete={Attaque: attaques, Parade: parades, Botte: bottes, Etape: etapes, Speciale: speciales}
for typeCarte in Carte.__subclasses__():
    d=mapClassCarteConcerteToDictObjectsCarteConcrete[typeCarte]
    for c in typeCarte.__subclasses__():
        carte=c()
        cartes.update({c: carte})
        d.update({c: carte})
del d,carte,typeCarte,c



def getNombreTotalCartes(partie: Partie = None):
    nbCartes = 0
    for c in cartes.values():
        nbCartes += c.getNombre(partie)
    return nbCartes
