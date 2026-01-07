import random
from heros import *
from grille import *
from objet import *

from params import *

import time
import os

SIZE_GRILLE = 16

class Controleur:
    def __init__(self, grille, ):
        self.l_heros = []
        self.grille = grille
        self.vague = 1
        self.score = 0
        self.score_final = 0
        self.tour = 1
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
    
    def get_score_final(self):
        return self.score_final
    
    def peut_deplacer(self, i, j, indice):
        global SIZE_GRILLE
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
            n = randint(0,3)
            (i,j) = convertit_depl(n)
            if(self.peut_deplacer(i,j,indice)):
                k = self.l_heros[indice].pos[0]
                l = self.l_heros[indice].pos[1]
                self.grille.get_case(k,l).remove_heros(self.l_heros[indice])
                self.l_heros[indice].pos = (k+i, l+j)
                self.grille.get_case(k+i,l+j).add_objet(self.l_heros[indice])
                boucle = False
    
    def ajouter_heros(self,heros):
        self.l_heros.append(heros)

    def vague_jeu(self):
        time.sleep(2)
        entree = self.grille.get_entree()
        self.l_heros = []
        for i in range(self.vague):
            self.ajouter_heros(Heros(entree[0],entree[1],[DeathObserver(), TreasureObserver()]))
        self.partie = True

    def set_score(self):
        heros = self.get_liste()
        observeurs = []
        for i in range(len(heros)):
            l = heros[i].get_obs()
            for j in range(len(l)):
                observeurs.append(l[j])
        self.score = 0
        for i in range(len(observeurs)):
            self.score += observeurs[i].get_value()
        self.score += self.score_final
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
        for i in range(len(indices_morts)):
            grille.get_case(x,y).remove_objet(L[indices_morts[i]])


    def set_score_final(self, n):
        self.score_final = n

    def aug_vague(self):
        self. vague += 1

    def change_tour(self):
        self.tour += 1
        self.tour = self.tour % 2





def convertit_depl(n):
    if(n == 0): #UP
        return(-1,0)
    elif(n == 1): #DOWN
        return(1,0)
    elif(n == 2): #LEFT
        return(0,-1)
    else: #RIGHT
        return(0,1)
    


def boucle_jeu(controleur):
    partie = True
    joue = "Héros"
    while(partie):
        os.system('cls' if os.name == 'nt' else 'clear')
        controleur.get_grille().affichage()
        score = controleur.set_score()
        print(f"Tour de {joue}")
        print(f"Vague : {controleur.get_vague()}                        Score : {score}")
        positions = ""
        for i in range(len(controleur.get_liste())):
            positions += "Position héros " + str(i+1) + " : " + str(controleur.get_liste()[i].get_pos()) + "     "
        print(f""+positions)
        print()
        print("\nCommandes :")
        print(f"C         :   Continuer la vague")
        print(f"S         :   Sauvegarder")
        print(f"Q         :   Quitter")
        action = input("\nCommande >").strip().upper()
        partie = controleur.get_partie()
        if action == 'C':
            if controleur.get_tour() == 0:
                controleur.check_collisions()
                joue = "Héros"
            else:
                controleur.depl_alea()
                joue = "Donjon"
            score = controleur.set_score()
            controleur.change_tour()
        elif action == 'Q' :
                controleur.partie = False
                controleur.set_score_final(controleur.get_score())
                return("Q")
        elif action == 'S':
            #sauvegarder la partie
            return("S")
        else:
            print(f"Pas d'action pour cette touche.")
            time.sleep(1)
    return("F")



def vagues(grille):
    controleur = Controleur(grille)
    boucle = True
    while(boucle and controleur.get_vague() <= 3):
        os.system('cls' if os.name == 'nt' else 'clear')
        controleur.vague_jeu()
        arrivee = boucle_jeu(controleur)
        os.system('cls' if os.name == 'nt' else 'clear')
        score = controleur.get_score_final()
        print(f"Vague {controleur.get_vague()} terminée")
        print(f"                            Score : {score}")
        if(arrivee == "F"):
            print(f"P         :   Prochaine vague")
        if(arrivee != "S"):
            print(f"S         :   Sauvegarder")
        else:
            print(f"Partie sauvegardée.")
        print(f"Q         :   Quitter")
        action = input("\nCommande >").strip().upper()
        if action == "P" and arrivee == "F":
            controleur.aug_vague()
        elif action == "S" and arrivee != "S":
            print("Partie sauvegardée.")
            boucle = False
            #sauvegarder
            pass
        elif action == "Q":
            boucle = False
        else:
            print(f"Pas d'action pour cette touche.")
            time.sleep(3)


if __name__ == "__main__":
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    vagues(grille)