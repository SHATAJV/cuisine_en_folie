class Appareil:
    """
    A class representing a kitchen appliance that can mix ingredients.

    Attributes:
        ingredients (list): A list to store the ingredients added to the appliance.
    """

    def __init__(self):
        """
        Initializes a new instance of the Appareil class with an empty list of ingredients.
        """
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):
        """
        Adds an ingredient to the list of ingredients.

        Args:
            ingredient (str): The ingredient to be added.
        """
        self.ingredients.append(ingredient)

    def melanger(self):
        """
        Mixes the ingredients and prints them out. If no ingredients are added,
        a message indicating that there are no ingredients to mix is printed.
        """
        if not self.ingredients:
            print("No ingredients to mix.")
            return

        print("Mixing ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
