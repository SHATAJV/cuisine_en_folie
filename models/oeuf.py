from models.ingrediants import Ingredient

class Oeuf(Ingredient):
    """
    Represents an egg as an ingredient.

    Inherits from:
        Ingredient: The base class representing an ingredient with a name, quantity, and unit.

    Attributes:
        quantity (int): The number of eggs.
    """

    def __init__(self, quantity: int):
        """
        Initializes the Oeuf ingredient with the specified quantity.

        Args:
            quantity (int): The number of eggs.
        """
        super().__init__(name="Oeuf", quantity=quantity, unit="nombre")

    def use(self):
        """
        Prints a message indicating the use of the specified number of eggs.

        Outputs:
            Prints a message about the number of eggs being used.
        """
        print(f"Utilisation des {self.quantity} oeufs.")
