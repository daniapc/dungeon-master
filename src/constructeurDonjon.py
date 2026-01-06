from src.objet import *
from src.fabrique_objet import *
from src.params import *
from src.grille import *

class ConstructeurDonjon :
    
    def __init__(self, grille, budget=BUDGET_INITIAL) :
        self.grille = grille 
        self.budget = budget
        self.fabrique_mur = Fabrique_Mur()
        self.fabrique_piege_1 = Fabrique_Piege_1()
        self.fabrique_piege_2 = Fabrique_Piege_2()
        self.fabrique_piege_3 = Fabrique_Piege_3()
    
    def get_budget(self) :
        return self.budget
    
    def is_in_grid(self, i, j) :
        if (0 <= i < SIZE_GRILLE and 0 <= j < SIZE_GRILLE) :
            return True 
        return False 
    
    def is_empty(self, i, j) :
        case = self.grille.get_case(i, j)
        if case.is_entree() or case.is_tresor() or len(case.objets) > 0 :
            return False 
        return True

    def put_mur(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Emplacement hors limites"
        if not self.is_empty(i, j) :
            return False, "Emplacement déjà occupé"
        mur = self.fabrique_mur.fabrique_Objet(i, j)
        cout = mur.get_cout()
        if self.budget >= cout :
            self.grille.get_case(i, j).add_objet(mur)
            self.budget -= cout 
            return True, "Mur placé"
        else :
            return False, "Budget insuffisant"
    
    def put_piege(self, i, j, type_piege) :
        if not self.is_in_grid(i, j) :
            return False, "Emplacement hors limites"
        if not self.is_empty(i, j) :
            return False, "Emplacement déjà occupé"
        if type_piege == 1 :
            piege = self.fabrique_piege_1.fabrique_Objet(i, j)
        if type_piege == 2 :
            piege = self.fabrique_piege_2.fabrique_Objet(i, j)
        if type_piege == 3 :
            piege = self.fabrique_piege_3.fabrique_Objet(i, j)
        cout = piege.get_cout()
        if self.budget >= cout :
            self.grille.get_case(i, j).add_objet(piege)
            self.budget -= cout 
            return True, f"Piège {type_piege} placé"
        else :
            return False, "Budget insuffisant"
        
    def rm_objet(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Case hors limites"
        if self.is_empty(i, j) :
            return False, "Case déjà vide"
        cout = self.grille.get_case(i ,j).get_objets()[0].get_cout()
        self.budget += cout
        self.grille.get_case(i ,j).remove_objet(self.grille.get_case(i ,j).get_objets()[0])
        return True, "Objet retiré"