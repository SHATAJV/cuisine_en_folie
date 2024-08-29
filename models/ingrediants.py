from abc import ABC, abstractmethod


class Ingredient(ABC):

    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @abstractmethod
    def use(self):
        pass
