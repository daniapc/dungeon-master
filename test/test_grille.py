from src.grille import *

def test_init_grille() :
    grille = Grille() 
    assert len(grille.get_grille()) == len(grille.get_grille()[0]) and len(grille.get_grille()[0]) == SIZE_GRILLE
    assert type(grille.get_grille()[0][0]) == Case

def test_entree() :
    grille = Grille()
    grille.put_entree()
    i, j = grille.get_entree()
    assert 0 <= i < SIZE_GRILLE and 0 <= j < SIZE_GRILLE    

def test_tresor() :
    grille = Grille()
    grille.put_entree()
    grille.put_tresor()
    i, j = grille.get_entree()
    it, jt = grille.get_tresor()
    assert 0 <= it < SIZE_GRILLE and 0 <= jt < SIZE_GRILLE
    assert abs(i - it) + abs(j - jt) > 4

