from abc import abstractmethod

class Objet:
    def __init__(self,x, y):
        self.pos = (x,y)

    def get_pos(self):
        return self.pos

class Mur(Objet):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.cout = 5
    
    def get_cout(self):
        return self.cout

    def affichage_mur(self):
        return "#"

class Piege(Objet):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.difficulte = 1
        self.active = True
    
    @abstractmethod
    def degat(self)->int: pass


class Piege_1(Piege):
    def __init__(self, x, y, difficulte):
        super().__init__(x,y,difficulte)
        self.cout = self.difficulte * 10
    
    def get_cout(self):
        return self.cout
    
    def degat(self):
        self.active = False
        return 10 * self.difficulte
    
    def affichage(self):
        return "_"

class Piege_2(Piege):
    def __init__(self, x, y, difficulte):
        super().__init__(x,y,difficulte)
        self.cout = self.difficulte * 10
        self.num_max_attaque = 2
    
    def get_cout(self):
        return self.cout
    
    def degat(self):
        if self.num_max_attaque > 0:
            self.num_max_attaque -= 1
            return 10 * self.difficulte

    def affichage(self):
        return "^"
    
class Piege_3(Piege):
    def __init__(self, x, y, difficulte):
        super().__init__(x,y,difficulte)
        self.cout = self.difficulte * 10
    
    def get_cout(self):
        return self.cout
    
    def degat(self):
        self.active = False
        return 30 * self.difficulte

    def affichage(self):
        return "¤"