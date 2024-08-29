import threading
import time

from models.commis import Commis


class Verseur(Commis, threading.Thread):
    """
    Represents a kitchen assistant responsible for pouring an ingredient from one container to another.

    Inherits from:
        Commis: The base class representing a kitchen assistant.
        threading.Thread: To allow the pouring action to run in a separate thread.
    """

    def __init__(self, name, source, destination, rate):
        """
        Initializes the Verseur with a name, source, destination, and pouring rate.

        Args:
            name (str): The name of the Verseur.
            source (Recipient): The source container.
            destination (Recipient): The destination container.
            rate (int): The rate of pouring per second (in units).
        """
        Commis.__init__(self, name)
        threading.Thread.__init__(self)
        self.source = source
        self.destination = destination
        self.rate = rate

    def run(self):
        """
        Executes the pouring action in a separate thread.

        Outputs:
            Prints a message indicating the progress of pouring.
        """
        global lock
        with lock:
            quantity_to_verser = self.source.content.quantity
            while quantity_to_verser > 0:
                amount_to_verse = min(self.rate, quantity_to_verser)
                print(
                    f"{self.name} verse {amount_to_verse} grammes de {self.source.content.name} dans le {self.destination.name}")
                quantity_to_verser -= amount_to_verse
                time.sleep(1)
            print(f"{self.name} a terminé de verser le contenu.")
