# https://www.geeksforgeeks.org/python/enum-in-python/
from enum import Enum

class Mode(Enum):
    TER = 1
    WEB = 2
    
    
print(Mode.TER.value)

print(Mode(1).name)


