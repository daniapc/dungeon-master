from flask import Flask, render_template
# https://flask.palletsprojects.com/en/stable/views/
from flask.views import MethodView

app = Flask(__name__)

from src.enums.mode import Mode

from src.log import Log
from src.grille import Grille

import io
import logging
import threading
import time
import os

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

    def get(self):
        return render_template('jeu.html')
    
    def set_mode(self, mode):
        self.mode = mode
    def get_mode(self):
        return self.mode
    
    def set_grille(self, gr):
        self.grille = gr
    
    def log(self, message):
        logging.info(message)

    def terminal_loop(self):
        time.sleep(1)  
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            self.grille.put_entree()
            self.grille.put_tresor()
            self.grille.affichage()
            
            action = input("Continue? Y/N ")
            
            self.log("Action: " + action)
            
            if action.upper() == 'N':
                os._exit(0)
    


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
       
    app.run(
        host='0.0.0.0', 
        port=5000,
        debug=not is_prod,  # prod
        use_reloader=False)

