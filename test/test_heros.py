from src.heros import *
from src.dmg_visitor import *

def test_init():
    heros = Heros(0,0,[])
    i = heros.get_pos()
    pv = heros.get_pv()
    assert(i == (0,0))
    assert(pv == 100)

def test_degats():
    heros = Heros(0,0,[])
    heros.degat(20)
    assert(heros.get_pv() == 80)
    assert(heros.isdead() == False)
    heros.degat(100)
    assert(heros.get_pv() == 0)
    assert(heros.isdead() == True)




