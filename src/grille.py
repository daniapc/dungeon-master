import random as rd
from src.params import *
from src.case import Case

class Grille :

    def __init__(self) :
        self.terrain = [[Case() for _ in range(SIZE_GRILLE)] for _ in range(SIZE_GRILLE)]
    
    def put_entree(self) :
        self.pos_entree = []
        self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        if self.pos_entree[0] == 0 or self.pos_entree[0] == SIZE_GRILLE -1 :
            self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        else :
            self.pos_entree.append(rd.choice([0, SIZE_GRILLE -1]))
        self.terrain[self.pos_entree[0]][self.pos_entree[1]].set_entree() 

    def put_tresor(self) :
        self.pos_tresor = [rd.randint(0, 15), rd.randint(0, 15)]
        ecart_ligne = abs(self.pos_entree[0] - self.pos_tresor[0])
        ecart_colonne = abs(self.pos_entree [1] - self.pos_tresor[1])
        if ecart_ligne + ecart_colonne < 5 :
            self.put_tresor()
        else :
            self.terrain[self.pos_tresor[0]][self.pos_tresor[1]].set_tresor() 

    def get_entree(self) :
        return self.pos_entree[0], self.pos_entree[1]
    
    def get_tresor(self) :
        return self.pos_tresor[0], self.pos_tresor[1]
    
    def get_grille(self) :
        return self.terrain
    
    def print_terrain(self) :
        for i in self.terrain :
            str = ""
            for j in i :
                if j.is_entree() :
                    str += '0'
                elif j.is_tresor() :
                    str += '8'
                else :
                    str += '1' 
            print(str)

    def affichage(self) :
        for row in self.terrain :
            str_row = ""
            for case in row :
                str_row += case.affichage()
            print(str_row)

    