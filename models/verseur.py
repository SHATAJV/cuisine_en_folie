import threading
import time
from models.commis import Commis

# Global lock for thread synchronization
lock = threading.Lock()

class Verseur(Commis):
    """
    Represents a pourer that transfers content from a source to a destination at a specified rate.

    Inherits from:
        Commis: The base class representing a kitchen assistant.

    Attributes:
        source (Recipient): The container from which content is poured.
        destination (Recipient): The container into which content is poured.
        rate (float): The rate at which content is poured, in grams per second.
    """

    def __init__(self, name: str, source, destination, rate: float):
        """
        Initializes the Verseur with a name, source container, destination container, and pour rate.

        Args:
            name (str): The name of the pourer.
            source (Recipient): The container from which content is being poured.
            destination (Recipient): The container into which content is being poured.
            rate (float): The rate at which content is poured, in grams per second.
        """
        super().__init__(name)
        self.source = source
        self.destination = destination
        self.rate = rate

    def work(self):
        """
        Performs the task of pouring content from the source container to the destination container.

        This method transfers content in increments defined by the rate attribute,
        and handles the pouring process until the source container is empty.

        Outputs:
            Prints messages indicating the progress of pouring and when the process is complete.
        """
        global lock
        with lock:
            quantity_to_verser = self.source.content.quantity
            while quantity_to_verser > 0:
                amount_to_verse = min(self.rate, quantity_to_verser)
                print(f"{self.name} verse {amount_to_verse} grammes du {self.source.name} dans le {self.destination.name}")
                quantity_to_verser -= amount_to_verse
                time.sleep(1)
            print(f"{self.name} a terminé de verser le contenu.")
