from src.fabrique_heros import *
from src.fabrique_objet import *

def test_instance():
    fab_m = Fabrique_Mur()
    mur = fab_m.fabrique_Objet(1,1)

    assert isinstance(mur, Mur)
    assert mur.get_pos() == (1,1)

    fab_p1 = Fabrique_Piege_1()
    p1 = fab_p1.fabrique_Objet(0,0)
    assert isinstance(p1, Piege_1)

    obs = DeathObserver()
    obs2 = TreasureObserver()
    fab_h = Fabrique_Heros()
    h = fab_h.fabrique_Heros(0,0,[obs,obs2])
    assert isinstance(h, Heros)
    assert h.get_pv() == 100

def test_polymorphisme():
    liste_fabriques = [Fabrique_Mur(), Fabrique_Piege_1(), Fabrique_Piege_2()]
    objets_crees = []

    for fabrique in liste_fabriques:
        # On appelle la même méthode 'fabrique_Objet' quel que soit le type
        obj = fabrique.fabrique_Objet(0, 0)
        objets_crees.append(obj)
    
    assert len(objets_crees)==3
    assert isinstance(objets_crees[0], Mur)
    assert isinstance(objets_crees[1], Piege_1)



