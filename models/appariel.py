
class Appareil:
    def __init__(self):
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):

        self.ingredients.append(ingredient)

    def melanger(self):

        print("Mélange des ingrédients :")
        for ingredient in self.ingredients:
            print(f"- {ingredient.name}: {ingredient.quantity} {ingredient.unit}")
        print("L'appareil est prêt à être utilisé.")
