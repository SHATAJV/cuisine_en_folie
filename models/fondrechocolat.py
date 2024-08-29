from models.commis import Commis


class FondeurChocolat(Commis):
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    def work(self):
        print(f"{self.name} fait fondre {self.quantity} grammes de chocolat.")
