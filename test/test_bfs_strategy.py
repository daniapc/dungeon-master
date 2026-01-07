import pytest
from src.ia_strategy import BFS

# --- FONCTION UTILITAIRE (Fixture) ---
# Ce décorateur permet de réutiliser cette logique dans tous les tests
@pytest.fixture
def preparer_grille(mocker):
    """
    Permet de configurer le départ, l'arrivée et les murs
    """
    def _constructeur(start, end, murs):
        # 1. On crée le mock de la grille
        mock_grille = mocker.Mock()
        mock_grille.get_entree.return_value = start
        mock_grille.get_tresor.return_value = end

        # 2. La logique dynamique pour get_case(x, y)
        def side_effect_get_case(x, y):
            mock_case = mocker.Mock()
            # Si les coordonnées sont dans la liste des murs, has_mur() renvoie True
            if (x, y) in murs:
                mock_case.has_mur.return_value = True
            else:
                mock_case.has_mur.return_value = False
            return mock_case

        mock_grille.get_case.side_effect = side_effect_get_case
        return mock_grille
    
    return _constructeur

# --- LES TESTS ---

def test_bfs_chemin_direct(preparer_grille):
    """Vérifie un chemin simple sans obstacles"""
    # On prépare une grille : Départ (0,0), Fin (0,2), pas de murs
    grille = preparer_grille(start=(0,0), end=(0,2), murs=[])
    
    algo = BFS()
    chemin = algo.applique_stategie(grille)
    
    assert chemin == [(0,0), (0,1), (0,2)]

def test_bfs_contournement_mur(preparer_grille):
    """Vérifie que l'IA contourne un mur"""
    # Mur en (0,1) qui bloque le chemin direct
    murs = [(0, 1)]
    grille = preparer_grille(start=(0,0), end=(0,2), murs=murs)
    
    algo = BFS()
    chemin = algo.applique_stategie(grille)
    
    # Assertions simples et lisibles
    assert chemin is not None
    assert (0, 1) not in chemin  # On ne doit pas traverser le mur
    assert chemin[0] == (0, 0)   # Départ correct
    assert chemin[-1] == (0, 2)  # Arrivée correcte

def test_bfs_impossible(preparer_grille):
    """Vérifie le cas où le trésor est inaccessible"""
    # On enferme le départ avec des murs autour de (0,0)
    # (Supposons que les voisins sont (0,1), (1,0) etc.)
    murs_bloquants = [(0, 1), (1, 0), (1, 1)] 
    grille = preparer_grille(start=(0,0), end=(5,5), murs=murs_bloquants)
    
    algo = BFS()
    chemin = algo.applique_stategie(grille)
    
    assert chemin is None or chemin == []