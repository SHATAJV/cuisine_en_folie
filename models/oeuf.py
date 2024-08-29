from models.ingrediants import Ingredient

class Oeuf(Ingredient):
    def __init__(self, quantity):
        super().__init__(name="Oeuf", quantity=quantity, unit="nombre")

    def use(self):
        print(f"Utilisation des {self.quantity} oeufs.")
