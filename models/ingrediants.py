from abc import ABC, abstractmethod

class Ingredient(ABC):
    """
    Abstract base class representing a generic ingredient.

    Attributes:
        name (str): The name of the ingredient.
        quantity (float): The amount of the ingredient.
        unit (str): The unit of measurement for the ingredient.
    """

    def __init__(self, name: str, quantity: float, unit: str):
        """
        Initializes an Ingredient with its name, quantity, and unit.

        Args:
            name (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient.
            unit (str): The unit of measurement for the quantity.
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @abstractmethod
    def use(self):
        """
        Abstract method that must be implemented by subclasses.

        This method should define how the ingredient is used or applied.
        """
        pass
