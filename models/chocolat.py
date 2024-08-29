class Chocolat:
    """
    A class representing chocolate with a specified quantity.

    Attributes:
        quantity (float): The quantity of chocolate in grams.
        name (str): The name of the item, which is "Chocolat".
        unit (str): The unit of measurement for the quantity, which is "grammes".
    """

    def __init__(self, quantity: float):
        """
        Initializes a new instance of the Chocolat class.

        Args:
            quantity (float): The quantity of chocolate in grams.
        """
        self.name = "Chocolat"
        self.quantity = quantity
        self.unit = "grammes"

    def __str__(self):
        """
        Returns a string representation of the Chocolat instance.

        Returns:
            str: A string describing the quantity, unit, and name of the chocolate.
        """
        return f"{self.quantity} {self.unit} {self.name}"
