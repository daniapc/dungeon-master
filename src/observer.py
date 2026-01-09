from src.params import *


class Observer:
    def __init__(self):
        self.value = 0    
    def get_value(self):
        return self.value

class DeathObserver(Observer):
    def __init__(self):
        super().__init__()

    def dead(self):
        self.value += 500
        super().__init__()

    def treasure(self):
        self.value -= BUDGET_INITIAL

class BudgetObserver(Observer):
    def __init__(self):
        super().__init__()

    def budget(self, budget):
        self.value += budget
