from models.ingrediants import Ingredient


class Appareil:
    """
    Represents a device used to mix ingredients.

    Attributes:
        ingredients (list of Ingredient): A list of ingredients to be mixed.
    """

    def __init__(self):
        """
        Initializes the Appareil with an empty list of ingredients.
        """
        self.ingredients = []

    def ajouter_ingredient(self, ingredient: Ingredient):
        """
        Adds an ingredient to the list of ingredients.

        Args:
            ingredient (Ingredient): The ingredient to be added.
        """
        self.ingredients.append(ingredient)

    def melanger(self):
        """
        Mixes the ingredients and prints their details.

        Outputs:
            Prints a list of the ingredients with their names, quantities, and units.
        """
        print("Mixing the ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient.name}: {ingredient.quantity} {ingredient.unit}")
        print("The device is ready to use.")
