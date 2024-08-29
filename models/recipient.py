class Recipient:
    def __init__(self, name, content=None):
        self.name= name
        self.content = content

    def ajouter_content(self, ingredient):

        if self.content is None:
            self.content = ingredient
        else:
            print(f"Le récipient contient déjà: {self.content.name}")
            print(f"Ajout de {ingredient.name} à {self.name}")


    def afficher_contenu(self):

        if self.content:
            print(f"{self.name} contient : {self.content.name} ({self.content.quantity} {self.content.unit})")
        else:
            print(f"{self.name} est vide.")
