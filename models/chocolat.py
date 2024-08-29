from models.ingrediants import Ingredient


class Chocolat(Ingredient):
    def __init__(self, quantity):
        super().__init__(name="Chocolat", quantity=quantity, unit="gramme")

    def use(self):
        print(f"Utilisation des {self.quantity} grammes de chocolat.")
