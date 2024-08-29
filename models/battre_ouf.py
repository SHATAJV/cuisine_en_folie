import threading
import time
from models.commis import Commis
from models.oeuf import Oeuf


class BatteurOeufs(Commis):
    """
    A class representing an egg beater, inheriting from the Commis class.

    Attributes:
        name (str): The name of the beater.
        nb_oeufs (int): The number of eggs to be beaten.
        recipient (object): The recipient object where beaten eggs will be added.
    """

    def __init__(self, name: str, nb_oeufs: int, recipient):
        """
        Initializes a new instance of the BatteurOeufs class.

        Args:
            name (str): The name of the beater.
            nb_oeufs (int): The number of eggs to be beaten.
            recipient (object): The recipient object where beaten eggs will be added.
        """
        super().__init__(name)
        self.nb_oeufs = nb_oeufs
        self.recipient = recipient

    def run(self):
        """
        Executes the egg beating process. Prints progress updates for each egg being beaten,
        waits for 1 second per egg, and finally adds the beaten eggs to the recipient.

        The recipient's `ajouter_content` method is used to add the beaten eggs.
        """
        print(f"{self.name} starts beating {self.nb_oeufs} eggs.")
        for i in range(self.nb_oeufs):
            print(f"{self.name} is beating the eggs, round #{i + 1}")
            time.sleep(1)
        beaten_eggs = Oeuf(quantity=self.nb_oeufs)
        self.recipient.ajouter_content(beaten_eggs)
        print(f"{self.name} has finished beating the eggs.")
