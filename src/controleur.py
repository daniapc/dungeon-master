from random import *
from src.heros import *
from src.grille import *
from src.objet import Mur 
from src.params import *

class Controleur:
    def __init__(self, l_heros, grille, ):
        self.l_heros = l_heros
        self.grille = grille

    def get_liste(self):
        return self.l_heros
    
    def get_grille(self):
        return self.grille
    
    def peut_deplacer(self, i, j, indice):
        k = self.l_heros[indice].pos[0]
        l = self.l_heros[indice].pos[1]
        if((0 <= k+i <= SIZE_GRILLE-1) and (0 <= l+j <= SIZE_GRILLE-1)):
            case = self.grille.get_grille()[k+i][l+j].get_objets()
            for elt in case:
                if isinstance(elt, Mur):
                    return False
            return True
        return False
    
    def depl_alea(self):
        for i in range(len(self.l_heros)):
            self.depl_alea_hero(i)

    def depl_alea_hero(self, indice):
        boucle = True
        while(boucle):
            n = random.randint(0,3)
            (i,j) = convertit_depl(n)
            if(self.peut_deplacer(i,j,indice)):
                k = self.pos[0]
                l = self.pos[1]
                self.grille[k][l].remove_objet(Heros)
                self.l_heros[indice].pos = (k+i, l+j)
                self.grille[k][l].add_objet(self)
                boucle = False


def convertit_depl(n):
    if(n == 0): #UP
        return(-1,0)
    elif(n == 1): #DOWN
        return(1,0)
    elif(n == 2): #LEFT
        return(0,-1)
    else: #RIGHT
        return(0,1)