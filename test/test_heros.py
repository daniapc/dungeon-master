from pytest import *
from src.heros import *
from src.dmg_visitor import *

def test_init():
    heros = Heros((0,0))
    i = heros.get_pos()
    pv = heros.get_pv()
    assert(i == (0,0))
    assert(pv == 100)

def test_degats():
    heros = Heros((0,0))
    visitor = Dmg_Visitor()
    visitor.visit(heros)
    assert(heros.get_pv() == 80)
    assert(heros.isdead() == False)
    heros.degats(100)
    assert(heros.get_pv() == 0)
    assert(heros.isdead() == True)


def test_deplacement():
    heros = Heros((0,0))
    depl = convertit_depl(0)
    assert(heros.peut_deplacer(depl[0], depl[1],[]) == False)
    depl = convertit_depl(1)
    assert(heros.peut_deplacer(depl[0], depl[1],[]) == True)
    depl = convertit_depl(2)
    assert(heros.peut_deplacer(depl[0], depl[1],[]) == False)
    depl = convertit_depl(3)
    assert(heros.peut_deplacer(depl[0], depl[1],[]) == True)


