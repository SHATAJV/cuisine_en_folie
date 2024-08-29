class Oeuf:
    def __init__(self, quantity: int):
        self.name = "Oeuf"
        self.quantity = quantity
        self.unit = "nombre"

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"
