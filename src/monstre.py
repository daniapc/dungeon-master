from random import *
from src.observer import *
from src.params import *

SIZE_GRILLE = 16


class Monstre():
    def __init__(self, x,y):
        self.pos = (x,y)
        self.pv = 100
        self.target = None
        
    def get_pv(self):
        return self.pv
    
    def get_pos(self):
        return self.pos
    
    def get_cout(self) :
        return PRIX_MONSTRE
    
    def deplace(self, i, j):
        a = self.pos[0]
        b = self.pos[1]
        a += i
        b += j
        self.pos = (a,b)

    def affichage(self):
        return("M")
    