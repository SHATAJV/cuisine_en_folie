import threading
import time
from models.commis import Commis


class Verseur(Commis):
    """
    A class representing a pourer that transfers content from a source to a destination
    at a specified rate. Inherits from the Commis class and supports concurrent execution.

    Attributes:
        name (str): The name of the pourer.
        source (Recipient): The source from which content is poured.
        destination (Recipient): The destination to which content is poured.
        rate (int): The rate at which content is poured (quantity per second).
    """

    def __init__(self, name: str, source, destination, rate: int):
        """
        Initializes a new instance of the Verseur class.

        Args:
            name (str): The name of the pourer.
            source (Recipient): The source object from which content will be poured.
            destination (Recipient): The destination object to which content will be poured.
            rate (int): The rate at which content is poured, in units per second.
        """
        super().__init__(name)
        self.source = source
        self.destination = destination
        self.rate = rate

    def run(self):
        """
        Executes the content pouring process.

        Continuously pours content from the source to the destination at the specified rate.
        The process involves:
        - Checking if the source has content and the quantity is greater than zero.
        - Pouring the content from the source to the destination at the specified rate.
        - Updating the quantity of the item being poured.
        - Removing the item from the source if its quantity reaches zero.
        - Adding the item to the destination.
        - Pausing for 1 second between pours.

        Prints messages to indicate the progress of the pouring operation.
        """
        while self.source.content and self.source.content[0].quantity > 0:
            item = self.source.content[0]
            quantity_to_verser = min(self.rate, item.quantity)
            print(f"{self.name} pours {quantity_to_verser} {item.unit} of {item.name} into {self.destination.name}")
            item.quantity -= quantity_to_verser
            if item.quantity == 0:
                with self.source.lock:
                    self.source.content.pop(0)
            self.destination.ajouter_content(item)
            time.sleep(1)
        print(f"{self.name} has finished pouring the content.")
