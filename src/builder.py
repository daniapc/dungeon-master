from src.Objet.objet import *
from src.params import *
from src.grille import *

class ConstructeurDonjon :
    
    def __init__(self, grille, budget=BUDGET_INITIAL) :
        self.grille = grille 
        self.budget = budget
    
    def get_budget(self) :
        return self.budget
    
    def is_in_grid(self, i, j) :
        if (0 <= i < SIZE_GRILLE and 0 <= j < SIZE_GRILLE) :
            return True 
        return False 
    
    def is_empty(self, i, j) :
        case = self.grille.get_case(i, j)
        if case.is_entree() | case.is_tresor() | len(case.objets) > 0 :
            return False 
        return True

    def put_mur(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Emplacement hors limites"
        if not self.is_empty(i, j) :
            return False, "Emplacement déjà occupé"
        # CREATION DU MUR
        cout = mur.get_cout()
        if self.budget >= cout :
            self.grille.get_grille().get_case(i, j).add_objet(mur)
            self.budget -= cout 
            return True
        else :
            return False
    
    def put_piege(self, i, j, type_piege) :
        if not self.is_in_grid(i, j) :
            return False, "Emplacement hors limites"
        if not self.is_empty(i, j) :
            return False, "Emplacement déjà occupé"
        # CREATION DU PIEGE
        cout = piege.get_cout()
        if self.budget >= cout :
            self.grille.get_grille().get_case(i, j).add_objet(piege)
            self.budget -= cout 
            return True
        else :
            return False
        
    def rm_objet(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Case hors limites"
        if self.is_empty(i, j) :
            return False, "Case déjà vide"
        cout = self.grille.get_grille().get_case(i ,j).get_objets()[0].get_cout()
        self.budget += cout
        self.grille.get_grille().get_case(i ,j).get_objets().remove_objet(self.grille.get_grille().get_case(i ,j).get_objets()[0])
        return True