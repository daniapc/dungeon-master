from src.params import *
from src.heros import *
from src.objet import *

class Case :

    def __init__(self) :
        self.objets = []
        self.entree = False 
        self.tresor = False 

    def get_objets(self) :
        return self.objets

    def add_objet(self, objet) :
        self.objets.append(objet)

    def remove_objet(self, objet_to_remove) :
        for i in range(len(self.objets)) :
            if type(self.objets[i]) == type(objet_to_remove) :
                self.objets.pop(i) 
                break

    def remove_heros(self, heros) :
        for i in range(len(self.objets)) :
            if self.objets[i] == heros :
                self.objets.pop(i)
                break

    def set_entree(self) :
        self.entree = True

    def set_tresor(self) :
        self.tresor = True 

    def rm_entree(self) :
        self.entree = False

    def rm_tresor(self) :
        self.tresor = False 

    def is_entree(self) :
        return self.entree

    def is_tresor(self) :
        return self.tresor     

    def has_hero(self) :
        for objet in self.objets :
            if type(objet) == Heros :
                return True 
        return False   

    def has_mur(self) :
        for objet in self.objets :
            if type(objet) == Mur :
                return True 
        return False    

    def affichage(self) :
        for objet in self.objets :
            if isinstance(objet, Heros) :
                return Heros.affichage()
        if len(self.objets) > 0 :
            return self.objets[0].affichage()
        elif self.is_entree() :
            return "E"
        elif self.is_tresor() :
            return "T"
        else :
            return "·"
