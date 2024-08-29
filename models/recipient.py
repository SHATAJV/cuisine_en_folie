class Recipient:
    """
    Represents a container that can hold an ingredient.

    Attributes:
        name (str): The name of the container.
        content (Ingredient or None): The ingredient currently in the container, or None if empty.
    """

    def __init__(self, name: str, content=None):
        """
        Initializes the Recipient with a name and an optional initial content.

        Args:
            name (str): The name of the container.
            content (Ingredient or None): The initial content of the container, if any.
        """
        self.name = name
        self.content = content

    def ajouter_content(self, ingredient):
        """
        Adds an ingredient to the container. If the container already has content, it replaces it.

        Args:
            ingredient (Ingredient): The ingredient to be added to the container.

        Outputs:
            Prints a message if the container already has content and replaces it.
        """
        if self.content is None:
            self.content = ingredient
            print(f"Ajout de {ingredient.name} à {self.name}.")
        else:
            print(f"Le récipient contient déjà : {self.content.name}.")
            print(f"Remplacement par {ingredient.name} dans {self.name}.")
            self.content = ingredient

    def afficher_contenu(self):
        """
        Prints the current content of the container.

        Outputs:
            Prints the name, quantity, and unit of the content, or a message if the container is empty.
        """
        if self.content:
            print(f"{self.name} contient : {self.content.name} ({self.content.quantity} {self.content.unit})")
        else:
            print(f"{self.name} est vide.")
