from src.heros import *

class Fabrique_Heros():
    def fabrique_Heros(self, x, y, obs):
        # heros est crée à la position d'entrée du donjon
        return Heros(x,y, obs)
