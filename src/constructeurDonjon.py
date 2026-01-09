from src.objet import *
from src.fabrique_objet import *
from src.fabrique_monstres import *
from src.params import *
from src.grille import *
from src.sauvegarde import GestionSauvegarde

from flask.views import MethodView
from flask import request

class ConstructeurDonjon(MethodView):
    
    def __init__(self, grille, budget=BUDGET_INITIAL, instance=None) :
        self.grille = grille 
        self.budget = budget
        self.l_monstres = []
        self.fabrique_mur = Fabrique_Mur()
        self.fabrique_monstre = Fabrique_Monstre()
        self.fabrique_piege_1 = Fabrique_Piege_1()
        self.fabrique_piege_2 = Fabrique_Piege_2()
        self.fabrique_piege_3 = Fabrique_Piege_3()
        
        self.instance = instance
    
    def get_budget(self) :
        return self.budget
    def set_budget(self, bg):
        self.budget = bg
    
    def get_l_monstres(self) :
        return self.l_monstres
    
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
        
    def put_monstre(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Emplacement hors limites"
        if not self.is_empty(i, j) :
            return False, "Emplacement déjà occupé"
        monstre = self.fabrique_monstre.fabrique_Monstre(i, j)
        cout = monstre.get_cout()
        if self.budget >= cout :
            self.grille.get_case(i, j).add_objet(monstre)
            self.budget -= cout 
            self.l_monstres.append(monstre)
            return True, "Monstre placé"
        else :
            return False, "Budget insuffisant"
        
    def rm_objet(self, i, j) :
        if not self.is_in_grid(i, j) :
            return False, "Case hors limites"
        if self.is_empty(i, j) :
            return False, "Case déjà vide"
        cout = self.grille.get_case(i ,j).get_objets()[0].get_cout()
        self.budget += cout
        objet_to_remove = self.grille.get_case(i ,j).get_objets()[0]
        if isinstance(objet_to_remove, Monstre) :
            for i in range(len(self.l_monstres)) :
                if self.l_monstres[i] == objet_to_remove :
                    self.l_monstres.pop(i)    
        self.grille.get_case(i ,j).remove_objet(objet_to_remove)
        return True, "Case vidée"
    
    def save_donjon(self) :
        data_donjon = self.grille.to_dict()
        data_donjon["budget_dépensé"] = BUDGET_INITIAL - self.budget
        file_name = input("Nom de la sauvegarde : ")
        if not file_name :
            file_name = "donjon_defaut"
        GestionSauvegarde.sauvegarder_donjon(file_name, data_donjon)
        return f"Donjon sauvegardé : {file_name}.json"
        
    def load_donjon(self, file_name) :
        data_donjon = GestionSauvegarde.charger_donjon(file_name)
        if data_donjon :
            fabriques_piege = [self.fabrique_piege_1, self.fabrique_piege_2, self.fabrique_piege_3]
            self.grille.from_dict(data_donjon, self.fabrique_mur, fabriques_piege, self.fabrique_monstre)
            self.budget = BUDGET_INITIAL - data_donjon["budget_dépensé"]
            return True, "Donjon chargé"
        return False, "Erreur chargement"

    # N'EST PAS REBATISER OU SUPPRIMER
    def post(self):
        self = self.instance
        
        data = request.json
        
        action = data['action']
        objet = data['objet']
        coord_x = int(data['x'])
        coord_y = int(data['y'])
        
        if (action == 'put'):
            if objet == 'mur':
                self.put_mur(coord_y, coord_x)
                
            elif 'piege' in objet:
                piege = int(str(objet).split(' ')[1])
                self.put_piege(coord_y, coord_x, piege)
                
            return {"status": "success", "message": "Case mise a jour", "budget": self.get_budget()}, 200 
    
        return {"status": "ignored", "message": "Nothing happened", "budget": self.get_budget()}, 200

    # N'EST PAS REBATISER OU SUPPRIMER
    def delete(self):
        self = self.instance
        
        data = request.json
        
        coord_x = int(data['x'])
        coord_y = int(data['y'])
        
        success, message = self.rm_objet(coord_y, coord_x)
        
        if success:
            return {"status": "success", "message": message, "budget": self.get_budget()}, 200 
        
        return {"status": "ignored", "message": message, "budget": self.get_budget()}, 200 
    
    def get(self):        
        self = self.instance
        
        objet = request.args.get('objet')
        attribute = request.args.get('attribute')
        
        if (attribute == 'cout' and objet != 'supprimer'):
            cout = 0 
            if objet == 'mur':
                cout = Mur(0,0).get_cout()
                
            elif 'piege' in objet:
                piege = int(str(objet).split(' ')[1])
                
                match piege:
                    case 1:
                        cout = Piege_1(0,0).get_cout()
                    case 2: 
                        cout = Piege_2(0,0).get_cout()
                    case 3:
                        cout = Piege_3(0,0).get_cout()
            
            return {"status": "success", "message": "Cout a ete returné", "cout": cout}, 200 
        
        elif attribute == 'budget':
            return {"status": "success", "message": "Budget a ete returné", "budget": self.get_budget()}, 200 
        
        return {"status": "ignored", "message": "Nothing happened"}, 200
                
                
                                
