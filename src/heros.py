from random import *
from src.observer import *

SIZE_GRILLE = 16


class Heros():
    def __init__(self, x,y,observers):
        self.pos = (x,y)
        self.pv = 100
        self.obs = observers
        self.state = False
    
    def get_pv(self):
        return self.pv
        
    def get_pos(self):
        return self.pos
    
    def get_obs(self):
        return self.obs
    
    def get_state(self):
        return self.state
    
    def get_score(self):
        var = 0
        for i in range(len(self.obs)):
            var += self.obs[i].get_value()
        return var

    def isdead(self):
        if self.pv == 0 and self.state == False:
            self.state = True
            self.notifyDeathObserver()
        return self.state
 
    def at_treasure(self, x, y):
        if self.pos[0] == x and self.pos[1] == y:
            self.notifyTreasureObserver()
            return True
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
    
    def affichage():
        return("H")
    
    def notifyDeathObserver(self):
        for obs in self.obs:
            if(isinstance(obs,DeathObserver)):
                obs.dead()

    def notifyTreasureObserver(self):
        for obs in self.obs:
            if(isinstance(obs,TreasureObserver)):
                obs.treasure()

    


            


        