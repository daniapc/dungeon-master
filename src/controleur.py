import random
from src.heros import *
from src.grille import *
from src.objet import *
from src.params import *
import time
import os
from src.ia_strategy import *
from src.fabrique_heros import *
from src.sauvegarde import GestionSauvegarde
from src.fabrique_objet import *

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
        self.recap = { "nb_heros" : 0,
                       "nb_heros_total" : 0,
                       "nb_heros_morts": 0,
                       "nb_heros_morts_total" : 0,
                       "nb_piege_faible_active" : 0,
                       "nb_piege_faible_active_total" : 0,
                       "nb_piege_moyen_active" : 0,
                       "nb_piege_moyen_active_total" : 0,
                       "nb_piege_puissant_active" : 0,
                       "nb_piege_puissant_active_total" : 0,
                       "tresor_trouve" : False}
        
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
        
        for h in self.get_liste():
            l_depl = self.strategie.applique_strategie(self.grille, h)

            pos = h.get_pos()
            self.grille.get_case(pos[0], pos[1]).remove_heros(h)

            h.deplace(l_depl[0][0], l_depl[0][1])
            
            pos = h.get_pos()
            self.grille.get_case(pos[0], pos[1]).add_objet(h)

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
    
    def set_partie(self, pt):
        self.partie = pt
        self.tour = 1
    
    def get_score_final(self):
        return self.score_final
    
    def get_recap(self):
        return self.recap
    
    def set_recap(self, key):
        if key == "tresor_trouve" : 
            self.recap["tresor_trouve"] = True
        else:
            self.recap[key] += 1
            txt = key + "_total"
            self.recap[txt] += 1
    
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
        self.recap["nb_heros"] = self.vague
        self.recap["nb_heros_total"] += self.vague
        self.recap["nb_heros_morts"] = 0
        self.recap["nb_piege_faible_active"] = 0
        self.recap["nb_piege_moyen_active"] = 0
        self.recap["nb_piege_puissant_active"] = 0
        self.tour = 1

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

    def reset_recap(self):
        self.recap = { "nb_heros" : 0,
                       "nb_heros_total" : 0,
                       "nb_heros_morts": 0,
                       "nb_heros_morts_total" : 0,
                       "nb_piege_faible_active" : 0,
                       "nb_piege_faible_active_total" : 0,
                       "nb_piege_moyen_active" : 0,
                       "nb_piege_moyen_active_total" : 0,
                       "nb_piege_puissant_active" : 0,
                       "nb_piege_puissant_active_total" : 0,
                       "tresor_trouve" : False}

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
                    if isinstance(L[j], Piege_1):
                         self.set_recap("nb_piege_faible_active")
                    if isinstance(L[j], Piege_2):
                        self.set_recap("nb_piege_moyen_active")
                    if isinstance(L[j], Piege_3):
                        self.set_recap("nb_piege_puissant_active")
                    if(L[j].get_cout() != 4):
                        heros.degat(DEGATS_1)
                    else:
                        heros.degat(DEGATS_2)
                    if(not(L[i].is_active())):
                        indices_objets.append(j)
                    if heros.isdead():
                        if j not in indices_morts:
                            self.score_final += heros.get_score()
                            self.set_recap("nb_heros_morts")
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
    
    def depl_tour(self, indice, l_depl, tour):
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
                self.set_recap("tresor_trouve")
                return True
    
    def enleve_heros(self):
        for indice in range(len(self.l_heros)) :
            k = self.l_heros[indice].pos[0]
            l = self.l_heros[indice].pos[1]
            self.grille.get_case(k,l).remove_heros(self.l_heros[indice])

    
    # FLASK METHOD: N'EST PAS RETIRER OU REBAPTISER CE METHOD!
    def get(self):
        self = self.instance
                
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
            vague = str(self.get_vague())
            
            if not(self.get_partie()):
                vague += " (terminée)"
            
            return {"status": "success", "message": "2Vague value enviée", 'vague': vague}
        elif attribute == 'boucle':
            return {"status": "success", "message": "Boucle value enviée", 'boucle': self.get_boucle()}
        elif attribute == 'partie':
            return {"status": "success", "message": "Partie value enviée", 'partie': self.get_partie()}
        
        return {"status": "ignored", "message": "Nothing happened"}, 200
    
    # FLASK METHOD: N'EST PAS RETIRER OU REBAPTISER CE METHOD!
    def post(self):
        self = self.instance
        
        data = request.json
        
        action = data['action']

        if action == 'lancer':
            self.set_boucle(True)
            self.set_strategie(BFS())
            
            return {"status": "success", "message": "La vague a eté lancée"}, 200 
        elif action == 'continuer':
            fini = False
            
            if self.get_tour() == 0:
                self.check_collisions()
                if self.get_liste() == []:
                    self.partie = False
                if self.check_treso():
                    self.partie = False
                    self.set_score()
                    self.set_score_final(self.get_score())
                    self.enleve_heros()
                    # self.set_boucle(False)
                    
                    fini = True
                    
                self.update_compteur()
                joue = "Héros"
            else:
                # self.depl_alea()
                self.execute_strategie()
                joue = "Donjon"
            self.set_score()
            self.score = self.get_score() + self.get_score_final()
            self.change_tour()
            
            return {"status": "success", 
                    "message": "La vague a eté continué",
                    "joue": joue,
                    "score": self.score,
                    "fini": fini
                    }, 200 
        
        return {"status": "ignored", "message": "Nothing happened"}, 200
    
    def get_data_heros(self) :
        data = []
        for heros in self.l_heros :
            data.append({
                "x" : heros.pos[0],
                "y" : heros.pos[1],
                "pv" : heros.get_pv()
            })
        return data
    
    def save_current_game(self) :
        current_grille = self.grille.to_dict()
        strategie = type(self.strategie).__name__ 
        data_game = {
            "grille" : current_grille,
            "heros" : self.get_data_heros(),
            "vague" : self.vague,
            "score" : self.score_final,
            "tour" : self.tour,
            "compteur" : self.compteur,
            "strategie" : strategie
        }
        file_name = input("Nom de la sauvegarde : ")
        if not file_name :
            file_name = "name_defaut"
        GestionSauvegarde.sauvegarder_donjon(file_name, data_game)
        return file_name
    
    def load_game(self, file_name) :
        data_game = GestionSauvegarde.charger_donjon(file_name)
        if not data_game :
            return False, "Fichier introuvable"
        try :
            self.vague = data_game.get("vague", 1)
            self.score_final = data_game.get("score", 0)
            self.compteur = data_game.get("compteur", 0)
            strategie = data_game["strategie"]
            if strategie == "BFS" :
                self.set_strategie(BFS())
            elif strategie == "Dijkstra" :
                self.set_strategie(Dijkstra())
            #elif strategie == "A" :
                #self.set_strategie(A())
            fabrique_Mur = Fabrique_Mur()
            fabriques_pieges = [Fabrique_Piege_1(), Fabrique_Piege_2(), Fabrique_Piege_3()]
            self.l_heros = []
            data_heros = data_game.get("heros", [])
            for data_hero in data_heros :
                heros = self.fab.fabrique_Heros(data_hero["x"], data_hero["y"], [DeathObserver(), TreasureObserver()])
                heros.set_pv(data_hero["pv"])
                self.ajouter_heros(heros)
                self.grille.get_case(data_hero["x"], data_hero["y"]).add_objet(heros)
            return True, "Partie chargée"

        except KeyError as e :
            return False, f"Fichier de sauvegarde corrompu : {e}"
        except Exception as e :
            return False, f"Erreur lors du chargement : {e}"


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
    if controleur.get_tour() == 0:
        joue = "Donjon"
    else:
        joue = "Héros"
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
            positions += "Position héros " + str(i+1) + " (PV = " + str(controleur.get_liste()[i].get_pv()) + " ) " + " : " + str(controleur.get_liste()[i].get_pos()) + "     "
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
                    controleur.set_partie(False)
                if controleur.check_treso():
                    controleur.set_partie(False)
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
                controleur.set_partie(False)
                controleur.set_score()
                controleur.set_score_final(controleur.get_score())
                controleur.enleve_heros()
                return("Q")
        elif action == 'S':
            file_name = controleur.save_current_game()
            print(f"Partie sauvegardée : {file_name}.json")
            time.sleep(2)
            controleur.enleve_heros()
            return("S")
        else:
            print(f"Pas d'action pour cette touche.")
            time.sleep(1)
    controleur.set_score()
    controleur.set_score_final(controleur.get_score())
    controleur.enleve_heros()
    return("F")

def verifier_chem_possible(controleur):
    tester = BFS()
    chem_possible = tester.cherche_chemin(controleur.get_grille(), controleur.get_grille().get_entree())
    if chem_possible is not None:
        boucle = True
    else:
        boucle = False
        print(f"Pas de chemin laissé de l'entrée au trésor.")
        time.sleep(3)
    
    return boucle

def lancer_vagues(controleur, sauvegarde=False):
    boucle = verifier_chem_possible(controleur)
    controleur.set_boucle(boucle)
    while(controleur.get_boucle() and controleur.get_vague() <= 3):
        if not sauvegarde :
            controleur.vague_jeu()
        else :
            sauvegarde = False
        os.system('cls' if os.name == 'nt' else 'clear')
        ia = True
        while(ia):
            print(f"Choix de l'IA")
            print(f"C         :   Chemin le plus court")
            print(f"S         :   Chemin le plus sûr")
            print(f"I         :   Chemin le plus sûr et court")
            action = input("\nCommande >").strip().upper()
            if action == "C":
                controleur.set_strategie(BFS())
                ia = False
            elif action == "S":
                controleur.set_strategie(Dijkstra())
                ia = False
            elif action == "I":
                controleur.set_strategie(A())
            else:
                print(f"Pas d'action pour cette touche.")
                time.sleep(3)
        arrivee = boucle_jeu(controleur)
        boucle = True
        while(boucle):
            recap(controleur)
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
                boucle = False
            elif action == "S" and arrivee != "S":
                print("Partie sauvegardée.")
                time.sleep(3)
                controleur.set_boucle(False)
                boucle = False
                #sauvegarder
                pass
            elif action == "Q":
                controleur.reset_recap()
                controleur.set_boucle(False)
                boucle = False
            else:
                print(f"Pas d'action pour cette touche.")
                time.sleep(3)


def recap(controleur):
    os.system('cls' if os.name == 'nt' else 'clear')
    score = controleur.get_score_final()
    dico = controleur.get_recap()
    txt = ""
    print(f"Vague {controleur.get_vague()} terminée")
    txt = "Nombre de héros engagés : " + str(dico["nb_heros"]) + " ( " + str(dico["nb_heros_total"]) + " )"
    print(f"" + txt)
    txt = "Nombre de héros morts : " + str(dico["nb_heros_morts"]) + " ( " + str(dico["nb_heros_morts_total"]) + " )"
    print(f"" + txt)
    txt = "Nombre de pièges faibles activés : " + str(dico["nb_piege_faible_active"]) + " ( " + str(dico["nb_piege_faible_active_total"]) + " )"
    print(f"" + txt)
    txt = "Nombre de pièges moyens activés : " + str(dico["nb_piege_moyen_active"]) + " ( " + str(dico["nb_piege_moyen_active_total"]) + " )"
    print(f"" + txt)
    txt = "Nombre de pièges puissants activés : " + str(dico["nb_piege_puissant_active"]) + " ( " + str(dico["nb_piege_puissant_active_total"]) + " )"
    print(f"" + txt)
    if dico["tresor_trouve"]:
        print(f"Trésor trouvé : oui")
    else:
        print(f"Trésor trouvé : non")
    print()
    print(f"                            Score : {score}")


if __name__ == "__main__":
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    lancer_vagues(grille)