import random as rd

class Grille :

    def __init__(self) :
        self.terrain = [[0 for _ in range(15)] for _ in range(15)]
    
    def set_entree(self) :
        self.pos_entree = []
        self.pos_entree.append(rd.randint(0, 15))
        if self.pos_entree[0] == 0 | self.pos_entree[0] == 15 :
            self.pos_entree.append(rd.randint(0, 15))
        else :
            self.pos_entree.append(rd.choice([0, 15]))

    