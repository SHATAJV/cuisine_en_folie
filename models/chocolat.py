class Chocolat:
    def __init__(self, quantity: float):
        self.name = "Chocolat"
        self.quantity = quantity
        self.unit = "grammes"

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"
