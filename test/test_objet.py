from src.Objet.objet import *

def creation():
    m = Mur(1,1)
    p1 = Piege_1(0,1)
    p2 = Piege_2(1,0)
    p3 = Piege_3(2,1)
    return m,p1,p2,p3

def test_pos():
    m,p1,p2,p3 = creation()

    assert m.get_pos() == (1,1)
    assert p1.get_pos() == (0,1)
    assert p2.get_pos() == (1,0)
    assert p3.get_pos() == (2,1)

