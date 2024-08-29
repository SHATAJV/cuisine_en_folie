from models.commis import Commis


class BatteurOeufs(Commis):
    """
    Represents a kitchen assistant specialized in beating eggs.

    Inherits from:
        Commis: The base class representing a kitchen assistant.

    Attributes:
        name (str): The name of the assistant.
        nb_oeufs (int): The number of eggs to be beaten.
    """

    def __init__(self, name: str, nb_oeufs: int):
        """
        Initializes the BatteurOeufs with the assistant's name and number of eggs.

        Args:
            name (str): The name of the assistant.
            nb_oeufs (int): The number of eggs to be beaten.
        """
        super().__init__(name)
        self.nb_oeufs = nb_oeufs

    def work(self):
        """
        Performs the task of beating the eggs and prints the action.

        Outputs:
            Prints a message indicating the number of eggs being beaten by the assistant.
        """
        print(f"{self.name} bats les {self.nb_oeufs} oeufs.")
