import random as rd
from src.params import *
from src.case import Case

from flask.views import MethodView
import io
from contextlib import redirect_stdout

class Grille(MethodView):

    def __init__(self, instance=None) :
        self.terrain = [[Case() for _ in range(SIZE_GRILLE)] for _ in range(SIZE_GRILLE)]
        
        # important pour le flask
        self.instance = instance
    
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
                        color = BOLD + GREEN
                    case "#" :
                        color = WHITE
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
        

if __name__ == "__main__" :
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    grille.affichage()
    
    grille.get()