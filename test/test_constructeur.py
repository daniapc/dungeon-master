from src.constructeurDonjon import *

def test_init() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille) 
    assert constructeur.budget == BUDGET_INITIAL
    assert isinstance(constructeur.grille, Grille)
    assert isinstance(constructeur.fabrique_mur, Fabrique_Mur)
    assert isinstance(constructeur.fabrique_piege_1, Fabrique_Piege_1)
    assert isinstance(constructeur.fabrique_piege_2, Fabrique_Piege_2)
    assert isinstance(constructeur.fabrique_piege_3, Fabrique_Piege_3)

def test_budget() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille)
    assert constructeur.get_budget() == BUDGET_INITIAL
    constructeur.budget = 0
    assert constructeur.get_budget() == 0
    bool, msg = constructeur.put_mur(0, 0)
    assert bool == False 
    assert msg == "Budget insuffisant"

def test_verif_case() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille)
    bool = False
    bool_2 = False
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            bool = constructeur.is_in_grid(i, j)
            bool_2 = constructeur.is_empty(i, j)
            assert bool == True 
            assert bool_2 == True
    bool = constructeur.is_in_grid(-5, 0)
    assert bool == False 
    bool = constructeur.is_in_grid(SIZE_GRILLE, 0)
    assert bool == False
    bool = constructeur.is_in_grid(0, SIZE_GRILLE)
    assert bool == False 
    bool = constructeur.is_in_grid(SIZE_GRILLE * 2, SIZE_GRILLE * 2)
    assert bool == False
    constructeur.put_mur(0, 0)
    bool_2 = constructeur.is_empty(0 ,0)
    assert bool_2 == False

def test_put_mur() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille)
    bool = False 
    msg = ""
    constructeur.budget = 0
    bool, msg = constructeur.put_mur(0, 0)
    assert bool == False
    assert msg == "Budget insuffisant"
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 1000
            bool, msg = constructeur.put_mur(i, j)
            assert bool == True 
            assert msg == "Mur placé"
    bool, msg = constructeur.put_mur(-1, -1)
    assert bool == False
    assert msg == "Emplacement hors limites"
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 1000
            bool, msg = constructeur.put_mur(i, j)
            assert bool == False 
            assert msg == "Emplacement déjà occupé"

def test_put_piege() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille)
    bool = False 
    msg = ""
    constructeur.budget = 0
    bool, msg = constructeur.put_piege(0, 0, 1)
    assert bool == False
    assert msg == "Budget insuffisant"
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 1000
            bool, msg = constructeur.put_piege(i, j, 1)
            assert bool == True 
            assert msg == "Piège 1 placé"
    bool, msg = constructeur.put_piege(-1, -1, 1)
    assert bool == False
    assert msg == "Emplacement hors limites"
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 1000
            bool, msg = constructeur.put_piege(i, j, 1)
            assert bool == False 
            assert msg == "Emplacement déjà occupé"

def test_rm_objet() :
    grille = Grille()
    constructeur = ConstructeurDonjon(grille)
    bool = False 
    msg = ""
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 1000
            bool, msg = constructeur.put_mur(i, j)
    for i in range(SIZE_GRILLE) :
        for j in range(SIZE_GRILLE) :
            constructeur.budget = 0
            bool, msg = constructeur.rm_objet(i, j)
            assert bool == True
            assert msg == "Case vidée"
            assert constructeur.budget == PRIX_MUR
    bool, msg = constructeur.rm_objet(0, 0)
    assert bool == False 
    assert msg == "Case déjà vide"
