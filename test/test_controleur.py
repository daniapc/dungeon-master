from src.controleur import *

def test_deplacement():
    heros = Heros(0,0,[])
    grille = Grille()
    mur = Mur(0,1)
    grille.get_grille()[0][1].add_objet(mur)
    L = [heros]
    controleur = Controleur(L,grille)
    depl = convertit_depl(0)
    assert(controleur.peut_deplacer(depl[0], depl[1],0) == False)
    depl = convertit_depl(1)
    assert(controleur.peut_deplacer(depl[0], depl[1],0) == True)
    depl = convertit_depl(2)
    assert(controleur.peut_deplacer(depl[0], depl[1],0) == False)
    depl = convertit_depl(3)
    assert(controleur.peut_deplacer(depl[0], depl[1],0) == False)