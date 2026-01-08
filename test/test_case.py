from src.case import *

def test_case() :
    case = Case()
    assert type(case.objets) == list 
    assert len(case.objets) == 0

def test_entree() :
    case = Case()
    case.set_entree()
    assert case.is_entree() == True 
    case.rm_entree()
    assert case.is_entree() == False 

def test_tresor() :
    case = Case()
    case.set_tresor()
    assert case.is_tresor() == True 
    case.rm_tresor()
    assert case.is_tresor() == False 

def test_heros():
    case = Case()
    assert case.has_hero() == False
    case.add_objet(Heros(1,1,[]))
    assert case.has_hero() == True

def test_mur():
    case = Case()
    assert case.has_mur() == False
    case.add_objet(Mur(1,1))
    assert case.has_mur() == True

