from src.monstre import *
from src.heros import Heros

def test_monstre():
    m = Monstre(3,5)
    assert m.get_pv() == 100
    assert m.get_pos() == (3,5)
    assert m.get_target() == None
    assert m.get_tour() == False
    h = Heros(3,6,[])
    m.set_target(h)
    assert m.get_pos_target() == (3,6)
    m.update_tour()
    m.degat(10)
    assert m.get_tour() == True
    assert m.get_pv() == 90
    m.deplace(0,1)
    assert m.get_pos() == (3,6)
    m.reset_tour()
    assert m.isdead() == False
    m.degat(400)
    assert m.get_tour() == False
    assert m.isdead() == True