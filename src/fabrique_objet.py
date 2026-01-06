from src.objet import *

class Fabrique_Objet():

    @abstractmethod
    def fabrique_Objet(self, x, y):
        #les objets sont crées au moment de les placer sur le donjon
        pass

class Fabrique_Mur(Fabrique_Objet):
    
    def fabrique_Objet(self, x, y):
        return Mur(x,y)

class Fabrique_Piege_1(Fabrique_Objet):
    def fabrique_Objet(self, x, y):
        return Piege_1(x,y)

class Fabrique_Piege_2(Fabrique_Objet):
    def fabrique_Objet(self, x, y):
        return Piege_2(x,y)

class Fabrique_Piege_3(Fabrique_Objet):
    def fabrique_Objet(self, x, y):
        return Piege_3(x,y)