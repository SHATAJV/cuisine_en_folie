from models.ingrediants import Ingredient

class Chocolat(Ingredient):
    def __init__(self, quantity):
        super().__init__(name="Chocolat", quantity=quantity, unit="grammes")

    def use(self):
        print(f"Utilisation de {self.quantity} de chocolat.")
