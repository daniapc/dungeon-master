from random import *
from src.observer import *
from src.params import *

class Monstre():
    def __init__(self, x,y):
        self.pos = (x,y)
        self.pv = 100
        self.target = None
        self.tour = False
        self.skin = randint(0, 1)
        
    def get_pv(self):
        return self.pv
    
    def get_pos(self):
        return self.pos
    
    def set_target(self, i):
        self.target = i

    def get_pos_target(self):
        if self.target == None:
            return 0,0
        return self.target.get_pos()[0], self.target.get_pos()[1]
    
    def get_cout(self):
        return PRIX_MONSTRE
    
    def get_target(self):
        return self.target
    
    def get_tour(self):
        return self.tour
    
    def get_skin(self):
        return self.skin
    
    def update_tour(self):
        self.tour = True

    def reset_tour(self):
        self.tour = False
    

    def deplace(self, i, j):
        a = self.pos[0]
        b = self.pos[1]
        a += i
        b += j
        self.pos = (a,b)

    def affichage(self):
        return("M")
    
    def degat(self, n):
        if(self.pv < n):
            self.pv = 0
        else:
            self.pv -= n
    
    def isdead(self):
        if self.pv == 0:
            return True
        return False