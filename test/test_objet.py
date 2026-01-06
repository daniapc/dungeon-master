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

def test_difficulte_Piege():
    m,p1,p2,p3 = creation()

    p1.set_difficulte(2)
    assert p1.get_difficulte() == 2

def test_degat_Piege():
    m,p1,p2,p3 = creation()

    assert p1.degat() == 10
    assert p1.is_active() == False
    assert p3.degat() == 30 
    assert p3.is_active() == False

    assert p2.degat() == 10
    assert p2.is_active() == True
    p2.degat()
    assert p2.is_active() == False

def test_cout():
    m,p1,p2,p3 = creation()

    assert m.get_cout() == 5
    assert p1.get_cout() == 10

    p1.set_difficulte(2)
    assert p1.get_cout() == 20

def test_difficulte_degat():
    m,p1,p2,p3 = creation()

    p1.set_difficulte(2)

    assert p1.degat() == 20