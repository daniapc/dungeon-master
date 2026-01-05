from src.params import *

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

    def set_entree(self) :
        self.entree = True

    def set_tresor(self) :
        self.tresor = True  

    def is_entree(self) :
        return self.entree

    def is_tresor(self) :
        return self.tresor           
