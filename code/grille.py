import random as rd
from params import *

class Grille :

    def __init__(self) :
        self.terrain = [[0 for _ in range(SIZE_GRILLE -1)] for _ in range(SIZE_GRILLE -1)]
    
    def set_entree(self) :
        self.pos_entree = []
        self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        if self.pos_entree[0] == 0 | self.pos_entree[0] == SIZE_GRILLE -1 :
            self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        else :
            self.pos_entree.append(rd.choice([0, SIZE_GRILLE -1]))

    