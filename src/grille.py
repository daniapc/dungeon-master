import random as rd
from src.params import *
from src.case import Case

from flask.views import MethodView
from src.objet import Mur, Piege
from src.monstre import Monstre

class Grille(MethodView):

    def __init__(self, instance=None) :
        self.reset()
        
        # important pour le flask
        self.instance = instance
        
    def reset(self):
        self.terrain = [[Case() for _ in range(SIZE_GRILLE)] for _ in range(SIZE_GRILLE)]
    
    def put_entree(self) :
        self.pos_entree = []
        self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        if self.pos_entree[0] == 0 or self.pos_entree[0] == SIZE_GRILLE -1 :
            self.pos_entree.append(rd.randint(0, SIZE_GRILLE -1))
        else :
            self.pos_entree.append(rd.choice([0, SIZE_GRILLE -1]))
        self.terrain[self.pos_entree[0]][self.pos_entree[1]].set_entree() 

    def vide(self):
        pos_entree = self.get_entree()
        pos_tresor = self.get_tresor()
        self.reset()
        self.terrain[self.pos_entree[0]][self.pos_entree[1]].set_entree()
        self.terrain[self.pos_tresor[0]][self.pos_tresor[1]].set_tresor()

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
    
    def get_case(self, i, j) :
        return self.terrain[i][j]
    
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
        en_tete = "   "
        for j in range(len(self.terrain[0])) :
            en_tete += f"{GREY}{j % 10} {RESET}"
        print(en_tete)
        print(f"  {GREY}" + "--" * len(self.terrain[0]) + f"{RESET}")
        for i, row in enumerate(self.terrain) :
            str_row = f"{GREY}{i:<2}|{RESET}"
            for case in row :
                symbol = case.affichage()
                color = RESET
                match symbol :
                    case "H" :
                        color = BOLD + MAGENTA
                    case "#" :
                        color = DARK_GREEN
                    case "T" :
                        color = BOLD + YELLOW
                    case "E" :
                        color = BOLD + BLUE
                    case "_" | "^" |"¤" :
                        color = RED
                    case "·" :
                        color = GREY
                str_row += f"{color}{symbol}{RESET} "
            print(str_row)
       
    # DON'T CHANGE THE NAME OF THIS FUNCTION! IT'S DERIVED FROM FLASK     
    # this function returns the affichage of the grille to the html
    def get(self):
        self = self.instance
        
        terrain_array = []        
                
        for row in self.terrain:
            row_array = []
            
            for case in row:
                symbol = case.affichage()
                if symbol == 'M':
                    symbol = ('M1' 
                        if case.get_objets()[0].get_skin() == 1 
                        else 'M2')
                
                color = 'black'
                weight = 'normal'                
                
                match symbol :
                    case "H" :
                        color = ANSI_TO_CSS[GREEN]
                        weight = ANSI_TO_CSS[BOLD]
                    case "#" :
                        color = ANSI_TO_CSS[WHITE]
                    case "T" :
                        color = ANSI_TO_CSS[YELLOW]
                        weight = ANSI_TO_CSS[BOLD]
                    case "E" :
                        color = ANSI_TO_CSS[BLUE]
                        weight = ANSI_TO_CSS[BOLD]
                    case "_" | "^" |"¤" :
                        color = ANSI_TO_CSS[RED]
                    case "·" :
                        color = ANSI_TO_CSS[GREY]
                
                case_obj = {}
                case_obj['color'] = color
                case_obj['weight'] = weight
                case_obj['symbol'] = symbol
                
                row_array.append(case_obj)
            
            terrain_array.append(row_array)
        
        return terrain_array
        
    def to_dict(self) :
        data_cases  = []
        for i in range(len(self.terrain)) :
            for j in range(len(self.terrain[0])) :
                case = self.terrain[i][j]
                if len(case.objets) > 0 :
                    objet_to_save = None 
                    for objet in case.objets :
                        if type(objet).__name__ != "Heros" and type(objet).__name__ != "Monstre":
                            objet_to_save = objet
                            break
                    if objet_to_save :
                        type_obj = type(objet_to_save).__name__ 
                        data_objet = {
                            "x" : i,
                            "y" : j,
                            "type" : type_obj
                        }
                        data_cases.append(data_objet)
        return {
            "entree" : self.pos_entree,
            "tresor" : self.pos_tresor,
            "objets" : data_cases
        }
    
    def from_dict(self, data, fabrique_mur, fabrique_pieges) :
        self.reset()
        self.pos_entree = data["entree"]
        self.pos_tresor = data["tresor"]
        self.terrain[self.pos_entree[0]][self.pos_entree[1]].set_entree()
        self.terrain[self.pos_tresor[0]][self.pos_tresor[1]].set_tresor()
        for data_objet in data["objets"] :
            x, y = data_objet["x"], data_objet["y"]
            type_obj = data_objet["type"]
            if type_obj == "Mur" :
                objet = fabrique_mur.fabrique_Objet(x, y)
            elif type_obj == "Piege_1" :
                objet = fabrique_pieges[0].fabrique_Objet(x, y)
            elif type_obj == "Piege_2" :
                objet = fabrique_pieges[1].fabrique_Objet(x, y)
            elif type_obj == "Piege_3" :
                objet = fabrique_pieges[2].fabrique_Objet(x, y)
            self.terrain[x][y].add_objet(objet)
            
    def get_budget(self):
        budget = BUDGET_INITIAL
        
        for row in self.terrain:
            for case in row :
                objets = case.get_objets()
                if len(objets) > 0 :
                    objet = objets[0]
                    if isinstance(objet, (Mur, Piege, Monstre)):
                        budget -= objet.get_cout()
        
        return budget
