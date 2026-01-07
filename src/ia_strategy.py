from collections import deque
from src.params import *
from src.grille import *
from src.case import *

class IA_Stategy():
    def applique_stategie(self, grille):
        pass

class BFS(IA_Stategy):

    def voisins(self, pos):
        voisins = list()
        if pos[0]-1 >= 0:
            voisins.append((pos[0]-1, pos[1]))
        if pos[1]+1 <= SIZE_GRILLE:
            voisins.append((pos[0],pos[1]+1))
        if pos[0]+1 <= SIZE_GRILLE:
            voisins.append((pos[0]+1,pos[1]))
        if pos[1]-1 >= 0:
            voisins.append((pos[0], pos[1]-1))
        return voisins
    
    def cherche_chemin(self, grille):
        xe, xy = grille.get_entree()
        E = (xe, xy)
        xt, yt = grille.get_tresor()
        T = (xt, yt)

        p = {E: None}
        q = deque()
        chemin_trouve = False
        res = list()
        q.append(E)

        while q:
            curr = q.popleft()
            
            if curr == T:
                chemin_trouve = True
            else:
                for v in self.voisins(curr):
                    if not grille.get_case(v[0], v[1]).has_mur():
                        if v not in p:
                            p[v] = curr
                            q.append(v)

        if chemin_trouve:
            chemin = []
            e = T
            while e is not None:
                chemin.append(e)
                e = p[e]
            
            chemin.reverse()
            return chemin
        else:
            return None
    
    def applique_stategie(self, grille):
        chemin = self.cherche_chemin(grille)
        if chemin is None:
            return None
        l_depl = list()
        for i in range(1,len(chemin)):
            a = chemin[i], b = chemin[i-1]
            depl = (a[0] - b[0], a[1] - b[1])
            l_depl.append(depl)
        
        return l_depl

