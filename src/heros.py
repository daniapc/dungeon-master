from random import *


class Heros():
    def __init__(self, pos):
        self.pos = pos
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
    
    def peut_deplacer(self, i, j, grille):
        k = self.pos[0]
        l = self.pos[1]
        if((0 <= k+i <= 15) and (0 <= l+j <= 15)):
            # case = grille[k+i][l+j].get_objets
            # for elt in case:
                # if isinstance(elt, Mur):
                #     return False
            return True
        return False
        
    def deplace(self, i, j):
        self.pos[0] += i
        self.pos[1] += j

    def degats(self, n):
        if(self.pv < n):
            self.pv = 0
        else:
            self.pv -= n



def convertit_depl(n):
    if(n == 0): #UP
        return(-1,0)
    elif(n == 1): #DOWN
        return(1,0)
    elif(n == 2): #LEFT
        return(0,-1)
    else: #RIGHT
        return(0,1)
            


        