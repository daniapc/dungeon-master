from abc import abstractmethod

class Objet:
    def __init__(self,x, y):
        self.pos = (x,y)

    def get_pos(self):
        return self.pos

class Mur(Objet):
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def get_cout(self):
        return 5

    def affichage_mur(self):
        return "#"

class Piege(Objet):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.difficulte = 1
        self.active = True
    
    def set_difficulte(self, i):
        self.difficulte = i
    
    def get_difficulte(self):
        return self.difficulte
    
    def is_active(self):
        return self.active
    
    @abstractmethod
    def degat(self)->int: pass


class Piege_1(Piege):
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def get_cout(self):
        return self.difficulte * 10
    
    def degat(self):
        if self.is_active():
            self.active = False
            return 10 * self.difficulte
    
    def affichage(self):
        return "_"

class Piege_2(Piege):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.num_max_attaque = 2
    
    def get_cout(self):
        return self.difficulte * 15
    
    def degat(self):
        if self.is_active():
            if self.num_max_attaque > 1:
                self.num_max_attaque -= 1
            else:
                self.active = False
            
            return 10 * self.difficulte

    def affichage(self):
        return "^"
    
class Piege_3(Piege):
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def get_cout(self):
        return self.difficulte * 30
    
    def degat(self):
        if self.is_active():
            self.active = False
            return 30 * self.difficulte

    def affichage(self):
        return "¤"