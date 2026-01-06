from src.observer import *
from src.heros import *


def test_heros():
    mort = DeathObserver()
    treso = TreasureObserver()
    heros = Heros(0,0,[mort,treso])
    heros.degat(50)
    var = heros.isdead()
    assert(mort.get_value() == 0) 
    heros.degat(78)
    var = heros.isdead()
    assert(mort.get_value() == 100)
    heros.at_treasure(0,0)
    assert(treso.get_value() == -500)
    L = heros.get_obs()
    n = 0
    for i in range(len(L)):
        print(L[i].get_value())
        n += L[i].get_value()
    assert(n == -400)