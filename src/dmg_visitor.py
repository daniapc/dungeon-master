from src.objet import *
from src.heros import *

class Dmg_Visitor:
    def visit(self, obj,i=None):
        if i == None:
            obj.degat()
        else:
            obj.degat(i)

