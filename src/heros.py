from random import *

SIZE_GRILLE = 16


class Heros():
    def __init__(self, x,y):
        self.pos = (x,y)
        self.pv = 100
    
    def get_pv(self):
        return self.pv
        
    def get_pos(self):
        return self.pos

    def isdead(self):
        if self.pv == 0:
            return True
        else:
            return False
 
        
    def deplace(self, i, j):
        a = self.pos[0]
        b = self.pos[1]
        a += i
        b += j
        self.pos = (a,b)

    def degat(self, n):
        if(self.pv < n):
            self.pv = 0
        else:
            self.pv -= n
    
    def affichage(self):
        return("H")


            


        