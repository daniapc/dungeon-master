from src.dmg_visitor import *

def test_dmg_vis():
    visiteur = Dmg_Visitor()
    heros = Heros(0,1,[])
    piege = Piege_1(1,2)
    visiteur.visit(heros,30)
    assert(heros.get_pv() == 70)
    visiteur.visit(piege)
    assert(piege.is_active() == False)