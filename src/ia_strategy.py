from collections import deque
import heapq
from math import inf
from src.params import *
from src.grille import *
from src.case import *
from src.heros import Heros

class IA_Strategy():
    def voisins(self, pos):
        voisins = list()
        if pos[0]-1 >= 0:
            voisins.append((pos[0]-1, pos[1]))
        if pos[1]+1 < SIZE_GRILLE:
            voisins.append((pos[0],pos[1]+1))
        if pos[0]+1 < SIZE_GRILLE:
            voisins.append((pos[0]+1,pos[1]))
        if pos[1]-1 >= 0:
            voisins.append((pos[0], pos[1]-1))
        return voisins
    
    def cout_case(self,x, y, grille):
        objets = grille.get_case(x,y).get_objets()

        cout = 1 #par défaut

        for ob in objets:
            if isinstance(ob, Piege):
                cout += ob.get_cout()
            if isinstance(ob, Mur):
                cout = inf
        
        return cout
    
    def reconstruir_chemin(self, p, T):
        chemin = []
        while T is not None:
            chemin.append(T)
            T = p[T]
        
        chemin.reverse()
        return chemin
    
    def cherche_chemin(self, grille, start, end):
        pass

    def applique_strategie(self, grille, h):
        chemin = self.cherche_chemin(grille, h.get_pos(), grille.get_tresor())
        if chemin is None:
            return None
        l_depl = list()
        for i in range(1,len(chemin)):
            a = chemin[i]
            b = chemin[i-1]
            depl = (a[0] - b[0], a[1] - b[1])
            l_depl.append(depl)
        
        return l_depl

class BFS(IA_Strategy):
    def cherche_chemin(self, grille, start, end):
        '''
        :param start: coordonnées position du héros
        '''
        p = {start: None}
        q = deque()
        chemin_trouve = False
        res = list()
        q.append(start)

        while q:
            curr = q.popleft()
            
            if curr == end:
                chemin_trouve = True
            else:
                for v in self.voisins(curr):
                    if not grille.get_case(v[0], v[1]).has_mur():
                        if v not in p:
                            p[v] = curr
                            q.append(v)

        if not chemin_trouve:
            return None
        else:
            return self.reconstruir_chemin(p, end)


class Dijkstra(IA_Strategy):        
    def cherche_chemin(self, grille, start, end):
        p = {start: None}
        cout_min = {start:0}
        pq = [(0, start)]
        heapq.heapify(pq)

        while pq:
            curr_cout, curr = heapq.heappop(pq)

            if curr == end:
                break
            else:
                for v in self.voisins(curr):
                    nouv_cout = curr_cout + self.cout_case(v[0], v[1], grille)
                
                    if v not in cout_min or nouv_cout < cout_min[v]:
                        cout_min[v] = nouv_cout
                        p[v] = curr
                        heapq.heappush(pq, (nouv_cout, v))
        
        if end not in p:
            return None
        else:
            return self.reconstruir_chemin(p, end)

class A(IA_Strategy):
    def heuristique(self, start, tresor):
        '''
        :param start: Position actuelle
        :param tresor: Position du trésor
        :return d: Distance Manhatan
        '''
        return abs(start[0] - tresor[0]) + abs(start[1] - tresor[1])

    def cherche_chemin(self, grille, start, end):
        p = {start: None}
        cout_min = {start:0}
        pq = [(0, start)]
        heapq.heapify(pq)

        while pq:
            curr_cout, curr = heapq.heappop(pq)

            if curr == end:
                break

            else:
                for v in self.voisins(curr):
                    nouv_cout = curr_cout + self.cout_case(v[0], v[1], grille)
                
                    if v not in cout_min or nouv_cout < cout_min[v]:
                        cout_min[v] = nouv_cout
                        p[v] = curr

                        #calcul du coût réel (cout + heuristique) pour aller dans v
                        score = nouv_cout + self.heuristique(v, end)
                        heapq.heappush(pq, (score, v))
                        
        if end not in p:
            return None
        else:
            return self.reconstruir_chemin(p, end)