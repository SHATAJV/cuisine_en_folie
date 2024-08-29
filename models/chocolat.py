from models.ingrediants import Ingredient


class Chocolat(Ingredient):
    """
    Represents chocolate as an ingredient.

    Inherits from:
        Ingredient: The base class representing an ingredient with a name, quantity, and unit.

    Attributes:
        quantity (float): The amount of chocolate in grams.
    """

    def __init__(self, quantity: float):
        """
        Initializes the Chocolat ingredient with a specified quantity in grams.

        Args:
            quantity (float): The quantity of chocolate in grams.
        """
        super().__init__(name="Chocolat", quantity=quantity, unit="grammes")

    def use(self):
        """
        Prints a message indicating the amount of chocolate being used.

        Outputs:
            Prints a message about the quantity of chocolate used.
        """
        print(f"Utilisation de {self.quantity} de chocolat.")
