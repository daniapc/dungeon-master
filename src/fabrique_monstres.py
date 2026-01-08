from src.monstre import *

class Fabrique_Monstre():
    def fabrique_Heros(self, x, y, obs):
        # heros est crée à la position d'entrée du donjon
        return Monstre(x,y)