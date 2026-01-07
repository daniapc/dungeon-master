import pytest
from src.controleur import Controleur
from src.ia_strategy import *

# --- FIXTURE (Configuration avancée) ---
@pytest.fixture
def preparer_grille_ponderee(mocker):
    """
    Simule une grille avec des murs ET des objets coûteux (pièges).
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

# --- LES TESTS ---
def test_cout_case(preparer_grille_ponderee):
    pieges = [(0,1)]
    murs = [(0,2)]
    grille = preparer_grille_ponderee(start=(0,0), end=(0,3), murs=murs, pieges=pieges)

    algo = Dijkstra()

    assert algo.cout_case(0,1,grille) == 11
    assert algo.cout_case(0,2,grille) == inf

def test_dijkstra_evite_piege(preparer_grille_ponderee):
    """
    SCÉNARIO :
    E P . T  (E=Entree, T=Trésor)
    . . . .  (P=Piège)
    
    Chemin direct : (0,0) -> (0,1) -> (0,2) -> (0,3) [Distance 3]
    Mais imaginons un piège en (0,1).
    L'IA doit préférer faire un détour par le bas (1,1) pour l'éviter.
    """
    # On met un piège sur le chemin direct
    pieges = [(0, 1)] 
    grille = preparer_grille_ponderee(start=(0,0), end=(0,2), murs=[], pieges=pieges)
    
    algo = Dijkstra()
    chemin = algo.cherche_chemin(grille)
    
    # Vérifications
    assert chemin is not None
    assert (0, 1) not in chemin, "L'IA ne doit pas marcher sur le piège si un détour est possible"
    # Le chemin devrait contourner, par exemple : (0,0) -> (1,0) -> (1,1) -> (1,2) -> (0,2)
    assert len(chemin) > 3, "Le chemin doit être plus long que la ligne droite car il fait un détour"

def test_dijkstra_traverse_si_obligatoire(preparer_grille_ponderee):
    """
    SCÉNARIO : Le piège bloque le seul passage.
    E P T
    M M M
    
    L'IA DOIT traverser le piège car c'est le seul chemin.
    """
    # Murs tout autour sauf en (0,1) où il y a un piège
    # Simplifions : Départ (0,0), Fin (0,2). Mur en (1,0), (1,1), (1,2). Piège en (0,1).
    murs = [(1,0), (1,1), (1,2), (-1,0), (-1,1), (-1,2)] # Bloque le bas et le haut
    pieges = [(0, 1)]
    
    grille = preparer_grille_ponderee(start=(0,0), end=(0,2), murs=murs, pieges=pieges)
    
    algo = Dijkstra()
    chemin = algo.cherche_chemin(grille)
    
    assert chemin is not None
    assert (0, 1) in chemin, "L'IA doit traverser le piège si aucun autre chemin n'existe"

def test_dijkstra_mur_infranchissable(preparer_grille_ponderee):
    """Vérifie que Dijkstra respecte toujours les murs (Coût infini)"""
    murs = [(0, 1)]
    grille = preparer_grille_ponderee(start=(0,0), end=(0,2), murs=murs, pieges=[])
    
    algo = Dijkstra()
    chemin = algo.cherche_chemin(grille)
    
    assert (0, 1) not in chemin

def test_deplacer_heros(preparer_grille_ponderee):
    murs = [(0, 1)]
    grille = preparer_grille_ponderee(start=(0,0), end=(0,2), murs=murs, pieges=[])
    h = Heros(0,0, [])
    ctr = Controleur(grille)
    ctr.ajouter_heros(h)
    ctr.update_compteur()

    algo = Dijkstra()
    chemin = algo.cherche_chemin(grille)

    ctr.set_strategie(algo)

    while h.get_pos() != (0,2):
        ctr.execute_strategie()
        ctr.update_compteur()
        
    assert h.get_pos() == (0,2)