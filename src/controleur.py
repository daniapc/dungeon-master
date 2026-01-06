from random import *
from src.heros import *
from src.grille import *
from src.objet import *

SIZE_GRILLE = 16

class Controleur:
    def __init__(self, grille, ):
        self.l_heros = []
        self.grille = grille
        self.vague = 0
        self.score = 0
        self.tour = 0
        self.partie = True

    def get_liste(self):
        return self.l_heros
    
    def get_grille(self):
        return self.grille
    
    def get_vague(self):
        return self.vague
    
    def get_score(self):
        return self.score
    
    def get_tour(self):
        return self.tour
    
    def get_partie(self):
        return self.partie
    
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
    
    def ajouter_heros(self,heros):
        self.l_heros.append(heros)

    def vague_jeu(self):
        entree = self.grille.get_entree()
        self.l_heros = []
        for i in range(self.vague):
            self.ajouter_heros(Heros(entree[0],entree[1],[DeathObserver(), TreasureObserver()]))
        self.partie = True

    def set_score(self):
        observeurs = self.get_liste()
        self.score = 0
        for i in range(len(observeurs)):
            self.score += observeurs[i].get_value()
        #ATTENTION IL FAUDRA AUSSI LE BUDGET

    def check_collisions(self):
        l_heros = self.get_liste()
        grille = self.get_grille()
        indices_morts = []
        for i in range(len(l_heros)):
            heros = l_heros[i]
            (x,y) = heros.get_pos()
            L = grille.get_case(x,y).get_objets()
            for i in range(len(L)):
                if isinstance(L[i], Piege):
                    L[i].degats()
                    heros.degats(20)
                    if(not(L[i].is_active())):
                        grille.get_case(x,y).remove_objet(L[i])
                    if heros.isdead():
                        indices_morts.append(i)
        for i in range(len(L)):
            grille.get_case(x,y).remove_objet(L[indices_morts[i]])





def convertit_depl(n):
    if(n == 0): #UP
        return(-1,0)
    elif(n == 1): #DOWN
        return(1,0)
    elif(n == 2): #LEFT
        return(0,-1)
    else: #RIGHT
        return(0,1)
    


def boucle_jeu(grille):
    controleur = Controleur(grille)
    partie = controleur.get_partie()
    controleur.get_grille().affiche()
    action = []
    while(partie):
        if action == "jouer": #PEUT ETRE A MODIFIER LE TITRE
            tour = controleur.get_tour()
            if tour == 0:
                controleur.check_collisions()
                #ennemis : vérifier collisions avec héros
                pass
            else:
                controleur.depl_alea()
                pass
            score = controleur.set_score
            tour += 1
            tour = tour % 2
        #demander la prochaine action
        partie = controleur.get_partie() #vérifier avanrt selon l'action




