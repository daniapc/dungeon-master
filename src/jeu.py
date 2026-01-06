from flask import Flask, render_template
# https://flask.palletsprojects.com/en/stable/views/
from flask.views import MethodView

app = Flask(__name__)

from src.enums.mode import Mode

from src.log import Log
from src.grille import Grille
from src.constructeurDonjon import ConstructeurDonjon
from src.params import *

import io
import logging
import threading
import time
import os

# (day_1)
# GEMINI { 
log_stream = io.StringIO()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    stream=log_stream  
)
# } GEMINI 

class Jeu(MethodView, object):
    _instance = None

    # https://python-patterns.guide/gang-of-four/singleton/
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Jeu, cls).__new__(cls)            
            
        return cls._instance
    
    def set_mode(self, mode):
        self.mode = mode
    def get_mode(self):
        return self.mode
    
    def set_grille(self, gr):
        self.grille = gr
        
    def set_constrDonjon(self, cd):
        self.constructeurDonjon = cd
    
    def log(self, message):
        logging.info(message)

    def terminal_loop(self):
        time.sleep(1)  

        self.constructeur = ConstructeurDonjon(self.grille)
        message = "Bienvenue Maitre du Donjon de la mort qui tue"

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("=== Crée ton Donjon ===")
            print(f"{message}")
            print(f"Budget : {self.constructeur.get_budget()}")
            print("")

            self.grille.affichage()
            
            print("\nCommandes :")
            print(f"M x,y     :   Placer Mur ({PRIX_MUR} fleurs)")
            print(f"P1 x,y    :   Placer Piège faible ({PRIX_P1} fleurs)")
            print(f"P2 x,y    :   Placer Piège moyen ({PRIX_P2} fleurs)")
            print(f"P3 x,y    :   Placer Piège puissant ({PRIX_P3} fleurs)")
            print(f"L         :   Lancer la vague")
            print(f"Q         :   Quitter")

            user_input = input("\nCommande >").strip().upper()
            if user_input == 'Q' :
                print("Fermeture du donjon")
                os._exit(0)
            elif user_input == 'L' :
                message = "Première vague"
            else :
                try :
                    cmd = user_input.split()
                    if len(cmd) < 2 :
                        message = "Format de commande invalide"
                        continue 
                    commande = cmd[0]
                    coor = cmd[1].split(',')
                    i = int(coor[0])
                    j = int(coor[1])
                    succes = False 
                    msg = ""
                    if commande == 'M' :
                        succes, msg = self.constructeur.put_mur(i, j)
                    elif commande == 'P1' :
                        succes, msg = self.constructeur.put_piege(i, j, 1)
                    elif commande == 'P2' :
                        succes, msg = self.constructeur.put_piege(i, j, 2)
                    elif commande == 'P3' :
                        succes, msg = self.constructeur.put_piege(i, j, 3)
                    elif commande == 'R' :
                        succes, msg = self.constructeur.rm_objet(i, j)
                    else :
                        msg = "Commande inconnue"
                    message = msg

                except ValueError :
                    message = "Erreur : Coordonnées invalides"
                except Exception as e :
                    message = f"Erreur : {e}"

            # self.grille.put_entree()
            # self.grille.put_tresor()
            
            # self.log("Action: " + action)
            
            # if action.upper() == 'N':
            #     os._exit(0)
    
if __name__ == "__main__":
    
    is_prod = os.environ.get('APP_ENV') == 'prod'
    
    mode = Mode.WEB.value if is_prod else input(
        "Indiquez le mode de jeu: [1] Terminal [2] Interface Web \n")
    
    jeu = Jeu()
    jeu.set_mode(Mode(int(mode)))
    
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    jeu.set_grille(grille)
    
    constrDonjon = ConstructeurDonjon(grille=grille)
    jeu.set_constrDonjon(constrDonjon)
        
    # (day_1)
    # GEMINI { 
    thread_terminal = threading.Thread(
            target=jeu.terminal_loop, 
            daemon=True
        )
    # } GEMINI 
    
    if (jeu.mode == Mode.TER):    
        thread_terminal.start()
    
    app.add_url_rule("/", view_func=Jeu.as_view("jeu"))
    app.add_url_rule("/logs", view_func=Log.as_view("logs", lg = log_stream))
    app.add_url_rule("/grille", view_func=Grille.as_view("grille", instance=grille))
    app.add_url_rule(
        "/constrdonjon", 
        view_func=ConstructeurDonjon.as_view("constrdonjon", grille=grille, instance=constrDonjon))
       
    app.run(
        host='0.0.0.0', 
        port=5000,
        debug=not is_prod,  # prod
        use_reloader=False)

