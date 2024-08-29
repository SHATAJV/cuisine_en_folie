class Oeuf:
    """
    A class representing eggs with a specified quantity.

    Attributes:
        quantity (int): The number of eggs.
        name (str): The name of the item, which is "Oeuf".
        unit (str): The unit of measurement for the quantity, which is "nombre" (number).
    """

    def __init__(self, quantity: int):
        """
        Initializes a new instance of the Oeuf class.

        Args:
            quantity (int): The number of eggs.
        """
        self.name = "Oeuf"
        self.quantity = quantity
        self.unit = "nombre"

    def __str__(self):
        """
        Returns a string representation of the Oeuf instance.

        Returns:
            str: A string describing the quantity, unit, and name of the eggs.
        """
        return f"{self.quantity} {self.unit} {self.name}"
