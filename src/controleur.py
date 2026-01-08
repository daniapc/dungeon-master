import random
from src.heros import *
from src.grille import *
from src.objet import *
from src.params import *
import time
import os
from src.ia_strategy import *
from src.fabrique_heros import *

from flask.views import MethodView
from flask import request

class Controleur(MethodView):
    def __init__(self, grille, budget, instance = None):
        self.l_heros = []
        self.grille = grille
        self.vague = 1
        self.score = 0
        self.score_final = budget
        self.tour = 1
        self.partie = True
        self.strategie = None
        self.compteur = 0
        self.fab = Fabrique_Heros()
        self.instance = instance
        
        self.boucle = False

    def get_liste(self):
        return self.l_heros
    
    def get_grille(self):
        return self.grille
    
    def get_fab(self): 
        return self.fab
    
    def set_strategie(self, strategie):
        self.strategie = strategie
    
    def update_compteur(self):
        self.compteur +=1
    
    def execute_strategie(self):
        if self.strategie is None:
            return
        
        l_depl = self.strategie.applique_strategie(self.grille)

        self.depl_tour_all(l_depl, self.compteur)

    def get_boucle(self):
        return self.boucle
    
    def set_boucle(self, bc):
        self.boucle = bc
    
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
        if((0 <= k+i < SIZE_GRILLE) and (0 <= l+j < SIZE_GRILLE)):
            case = self.grille.get_case(k+i, l+j).get_objets()
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
        entree = self.grille.get_entree()
        self.l_heros = []
        for i in range(self.vague):
            self.ajouter_heros(self.get_fab().fabrique_Heros(entree[0],entree[1],[DeathObserver(), TreasureObserver()]))
        self.partie = True
        self.compteur = 0

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
        # self.score += self.score_final
        #ATTENTION IL FAUDRA AUSSI LE BUDGET

    def check_collisions(self):
        l_heros = self.get_liste()
        grille = self.get_grille()
        indices_morts = []
        indices_objets = []
        for i in range(len(l_heros)):
            heros = l_heros[i]
            (x,y) = heros.get_pos()
            L = grille.get_case(x,y).get_objets()
            for j in range(len(L)):
                if isinstance(L[j], Piege):
                    L[j].degat()
                    heros.degat(20)
                    if(not(L[i].is_active())):
                        indices_objets.append(i)
                    if heros.isdead():
                        if j not in indices_morts:
                            self.score_final += heros.get_score()
                            indices_morts.append(j)
            for k in range(len(indices_objets)):
                grille.get_case(x,y).remove_objet(L[indices_objets[k]])
            L = [] 
        for i in range(len(indices_morts)):
            grille.get_case(x,y).remove_heros(self.l_heros[indices_morts[i]])
            self.l_heros.pop(indices_morts[i])

    def set_score_final(self, n):
        self.score_final += n

    def aug_vague(self):
        self. vague += 1

    def change_tour(self):
        self.tour += 1
        self.tour = self.tour % 2

    def depl_heros(self, indice, l_depl):
        if l_depl is None:
            return
        h = self.get_liste()[indice]

        for depl in l_depl:
            pos = h.get_pos()
            self.grille.get_case(pos[0], pos[1]).remove_heros(h)
            h.deplace(depl[0], depl[1])

            pos = h.get_pos()
            self.grille.get_case(pos[0], pos[1]).add_objet(h)
    
    def depl(self, l_depl):
        for i in range(len(self.l_heros)):
            self.depl_heros(i, l_depl)
    
    def depl_tour(self, indice,l_depl, tour):
        '''
        tour est le compteur de tour
        '''
        if tour > len(l_depl):
            return
        h = self.get_liste()[indice]

        pos = h.get_pos()
        self.grille.get_case(pos[0], pos[1]).remove_heros(h)

        h.deplace(l_depl[tour-1][0], l_depl[tour-1][1])

        pos = h.get_pos()
        self.grille.get_case(pos[0], pos[1]).add_objet(h)
    
    def depl_tour_all(self, l_depl, tour):
        for i in range(len(self.l_heros)):
            self.depl_tour(i, l_depl, tour)

    def check_treso(self):
        heros = self.l_heros
        tresor = self.grille.get_tresor()
        for i in range(len(heros)):
            if heros[i].at_treasure(tresor[0],tresor[1]):
                return True
    
    def enleve_heros(self):
        for indice in range(len(self.l_heros)) :
            k = self.l_heros[indice].pos[0]
            l = self.l_heros[indice].pos[1]
            self.grille.get_case(k,l).remove_heros(self.l_heros[indice])

    
    # FLASK METHOD: N'EST PAS RETIRER OU REBAPTISER CE METHOD!
    def get(self):
        self = (Controleur)(self.instance)
                
        attribute = request.args.get('attribute')
        
        if attribute == 'heros':
            liste = self.get_liste()
            heros = []
            for i in range(len(liste)):
                heros.append(
                    {
                        'index': i,
                        'x': liste[i].get_pos()[1],
                        'y': liste[i].get_pos()[0]
                    }
                )
            return {"status": "success", "message": "Heros list enviée", 'heros': heros}
        elif attribute == 'vague':
            return {"status": "success", "message": "Vague value enviée", 'vague': self.get_vague()}
        elif attribute == 'boucle':
            return {"status": "success", "message": "Boucle value enviée", 'boucle': self.get_boucle()}
        
        return {"status": "ignored", "message": "Nothing happened"}, 200
    
    # FLASK METHOD: N'EST PAS RETIRER OU REBAPTISER CE METHOD!
    def post(self):
        self = self.instance
        
        return {"status": "ignored", "message": "Nothing happened"}, 200

    


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
    controleur.set_strategie(BFS())
    while(partie):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"         === Vague : {controleur.get_vague()} ===")
        controleur.get_grille().affichage()
        controleur.set_score()
        score = controleur.get_score() + controleur.get_score_final()
        print(f"Tour de {joue}")
        print(f"Score : {score}")
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
                if controleur.get_liste() == []:
                    controleur.partie = False
                if controleur.check_treso():
                    controleur.partie = False
                    controleur.set_score()
                    controleur.set_score_final(controleur.get_score())
                    controleur.enleve_heros()
                    return("Q")
                controleur.update_compteur()
                joue = "Héros"
            else:
                # controleur.depl_alea()
                controleur.execute_strategie()
                joue = "Donjon"
            controleur.set_score()
            score = controleur.get_score() + controleur.get_score_final()
            controleur.change_tour()
        elif action == 'Q' :
                controleur.partie = False
                controleur.set_score()
                controleur.set_score_final(controleur.get_score())
                controleur.enleve_heros()
                return("Q")
        elif action == 'S':
            #sauvegarder la partie
            controleur.enleve_heros()
            return("S")
        else:
            print(f"Pas d'action pour cette touche.")
            time.sleep(1)
    controleur.set_score()
    controleur.set_score_final(controleur.get_score())
    controleur.enleve_heros()
    return("F")



def lancer_vagues(controleur: Controleur):
    controleur.set_boucle(True)

    while(controleur.get_boucle() and controleur.get_vague() <= 3):
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
            time.sleep(3)
            controleur.set_boucle(False)
            #sauvegarder
            pass
        elif action == "Q":
            controleur.set_boucle(False)
        else:
            print(f"Pas d'action pour cette touche.")
            time.sleep(3)


if __name__ == "__main__":
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    lancer_vagues(grille)