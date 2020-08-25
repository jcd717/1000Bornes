from moteur import cartes,attaques
from moteur.classes import *


def main():
    # p=Partie()
    # print(p.nombreJoueurs)

    # c=Accident()
    # print(c.typeName, c.nom, c.genre.name, c.getNombre(), c.getNombre(Partie(2)))
    nbCartes = 0
    for c in cartes.values():
        print(c.nom+':', c.getNombre(),c.typeName)
        nbCartes += c.getNombre()
    print('----------------')
    print(nbCartes)
    print('----------------')
    print()
    print('ATTAQUES')
    print('--------')
    for c in attaques.values():
        print(c.nom)
    print('----------------')
    print(issubclass(Accident, Carte))
    




if __name__ == "__main__":
    main()
