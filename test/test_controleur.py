import pytest
from src.controleur import *

def test_deplacement():
    heros = Heros(0,0,[])
    grille = Grille()
    mur = Mur(0,1)
    grille.get_grille()[0][1].add_objet(mur)
    controleur = Controleur(grille, 100,[])
    controleur.ajouter_heros(heros)
    
    depl = convertit_depl(0)
    h = controleur.get_liste()[0].get_pos()
    assert(controleur.peut_deplacer(depl[0], depl[1],h[0],h[1]) == False)
    depl = convertit_depl(1)
    assert(controleur.peut_deplacer(depl[0], depl[1],h[0],h[1]) == True)
    depl = convertit_depl(2)
    assert(controleur.peut_deplacer(depl[0], depl[1],h[0],h[1]) == False)
    depl = convertit_depl(3)
    assert(controleur.peut_deplacer(depl[0], depl[1],h[0],h[1]) == False)

@pytest.fixture
def preparer_grille_ponderee(mocker):
    """
    Simule une grille avec des murs ET des objets
    """
    def _constructeur(start, end, murs, pieges):
        # 1. Mock de la grille de base
        mock_grille = mocker.Mock()
        mock_grille.get_entree.return_value = start
        mock_grille.get_tresor.return_value = end

        # 2. Logique pour get_case(x, y)
        def side_effect_get_case(x, y):
            mock_case = mocker.Mock()
            mock_objets = []

            # Gestion des murs
            if (x, y) in murs:
                mock_mur = mocker.Mock(spec=Mur)
                mock_mur.get_cout.return_value = inf 
                mock_objets.append(mock_mur)

            # Gestion des pièges
            if (x, y) in pieges:
                mock_piege = mocker.Mock(spec=Piege)
                mock_piege.get_cout.return_value = 10   # Si vous utilisez .get_cout()
                mock_objets.append(mock_piege)
            
            mock_case.get_objets.return_value = mock_objets
            return mock_case

        mock_grille.get_case.side_effect = side_effect_get_case
        return mock_grille
    
    return _constructeur

def test_lancer_vagues_pas_de_chemin(preparer_grille_ponderee):
    '''
    SCÉNARIO :
    E M .
    M T M
    . M .

    Il n'y a pas de chemin pour atteindre le trésor
    '''
    murs = [(0,1),(1,0),(1,2),(2,1)]

    grille = preparer_grille_ponderee(start=(0,0), end=(1,1), murs=murs, pieges=[])
    c = Controleur(grille, 100,[])

    assert c.verifier_chem_possible()==False
    
