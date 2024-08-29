class Appareil:
    def __init__(self):
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def melanger(self):
        if not self.ingredients:
            print("Aucun ingrédient à mélanger.")
            return

        print("Mélange des ingrédients :")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
