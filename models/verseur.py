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
        super().__init__(name)
        self.source = source
        self.destination = destination
        self.rate = rate

    def run(self):
        """
        Executes the content pouring process.

        Continuously pours content from the source to the destination at the specified rate.
        Ensures that at least 30 grams of content remain in the source.
        """
        while self.source.content and self.source.content[0].quantity > 30:
            item = self.source.content[0]
            quantity_to_verser = min(self.rate, item.quantity - 30)  # Ensure 30g remains
            print(f"{self.name} pours {quantity_to_verser} {item.unit} of {item.name} into {self.destination.name}")
            item.quantity -= quantity_to_verser
            if item.quantity <= 30:  # Stop pouring when 30g or less remains
                break
            self.destination.ajouter_content(item)
            time.sleep(1)

        print(
            f"{self.name} has finished pouring the content. {self.source.content[0].quantity} {item.unit} of {item.name} remains in the source.")
