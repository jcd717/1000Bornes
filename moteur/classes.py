from enum import Enum, auto
from abc import ABC, abstractmethod
from .partie import Partie


class Genre(Enum):
    MASCULIN = auto()
    FEMININ = auto()


class Carte(ABC):  # ABC: Abstract Base Class = classe abstraite
    def __init__(self):
        self._typeName = None
        self._genre = None
        self._nombre = None
        self._nom = None

    @property
    def typeName(self):
        return self._typeName

    @property
    def genre(self):
        return self._genre

    def getNombre(self, partie: Partie = None):
        return self._nombre if partie == None else (
            self._nombre - (1 if isinstance(self, Attaque)
                            and partie.nombreJoueurs == 2 else 0)
        )

    @property
    def nom(self):
        return self._nom


class Attaque(Carte):
    def __init__(self):
        super().__init__()
        self._typeName = "Attaque"


class Parade(Carte):
    def __init__(self):
        super().__init__()
        self._typeName = "Parade"


class Botte(Carte):
    def __init__(self):
        super().__init__()
        self._typeName = "Botte"


class Etape(Carte):
    def __init__(self):
        super().__init__()
        self._typeName = "Étape"


class Speciale(Carte):  # l'image de "dos des cartes" par exemple
    def __init__(self):
        super().__init__()
        self._typeName = "Spéciale"



class Accident(Attaque):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "Accident"
        self._nombre = 3



class AsDuVolant(Botte):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "As du Volant"
        self._nombre = 1



class Citerne(Botte):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Citerne"
        self._nombre = 1



class Creve(Attaque):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "Crevé"
        self._nombre = 3



class Dos(Speciale):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "DOS"
        self._nombre = 0



class Essence(Parade):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Essence"
        self._nombre = 6



class Etape100(Etape):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "100"
        self._nombre = 12



class Etape200(Etape):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "200"
        self._nombre = 4



class Etape25(Etape):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "25"
        self._nombre = 10



class Etape50(Etape):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "50"
        self._nombre = 10



class Etape75(Etape):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "75"
        self._nombre = 10



class FeuRouge(Attaque):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "Feu Rouge"
        self._nombre = 5



class FeuVert(Parade):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "Feu Vert"
        self._nombre = 14



class FinDeLimitation(Parade):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Fin de Limitation"
        self._nombre = 6



class Increvable(Botte):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Increvable"
        self._nombre = 1



class LimitationDeVitesse(Attaque):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Limitation de Vitesse"
        self._nombre = 4



class PanneEssence(Attaque):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Panne d'Essence"
        self._nombre = 3



class PasDeCarte(Speciale):
    def __init__(self):
        super().__init__()
        self._genre = Genre.MASCULIN
        self._nom = "pas de carte"
        self._nombre = 0


class Prioritaire(Botte):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Prioritaire"
        self._nombre = 1



class Reparation(Parade):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Réparation"
        self._nombre = 6



class RoueDeSecours(Parade):
    def __init__(self):
        super().__init__()
        self._genre = Genre.FEMININ
        self._nom = "Roue de Secours"
        self._nombre = 6
