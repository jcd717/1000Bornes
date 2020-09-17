import sys,random
# si ce module est appelé depuis une GUI (appli Web par ex), il y a risque d'import circulaire
# if not 'moteur.classes' in sys.modules:
#     from .classes import Speciale

# if not 'moteur' in sys.modules:
#     from . import cartes

import moteur,moteur.classes



class Partie:

    class CartesEnMain:
        def __init__(self, partie):
            self.nbCartes = 6
            self._cartesEnMain=[]
            for _ in range(self.nbCartes):
                self._cartesEnMain.append(partie.tas.pop())

        @property
        def cartes(self):
            return self._cartesEnMain



    class Joueur:
        def __init__(self,partie):
            self.cartesEnMain=Partie.CartesEnMain(partie)


    def __init__(self, nombreJoueurs=4):
        self._nombreJoueurs = nombreJoueurs

        self._terminated=False

        # mélanger les cartes et les mettre dans la variable self.tas
        self.tas=[]
        for c in moteur.cartes.values():
            if not isinstance(c, moteur.classes.Speciale):
                for _ in range(c.getNombre(self)):
                    self.tas.append(c)
        random.shuffle(self.tas)

        # créer les joueurs (et donc distrubuer dans la classe Joueur)
        self.joueurs=[]
        for _ in range(self.nombreJoueurs):
            self.joueurs.append(Partie.Joueur(self))
        



    @property        
    def nbCartesRestantes(self):
        return len(self.tas)

    @property
    def terminated(self):
        return self._terminated
                
    

    @property
    def nombreJoueurs(self):
        return self._nombreJoueurs


