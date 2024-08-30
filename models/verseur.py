import threading
from models.chocolat import Chocolat
from models.commis import Commis
import time


class Verseur(threading.Thread):
    """
    A class representing a pouring mechanism that transfers a specified quantity of content from a source to a destination.

    The `Verseur` class is designed to simulate the action of pouring a specific quantity of content (e.g., melted chocolate)
    from one container (source) to another (destination). It operates in a separate thread to allow concurrent processing
    and uses thread-safe operations to manage content transfer.

    Attributes:
        name (str): The name of the verseur (pouring mechanism).
        source (Recipient): The source container from which content is poured.
        destination (Recipient): The destination container into which content is poured.
        rate (int): The rate at which content is poured per second (in grams).
        target_quantity (float): The total quantity of content to be poured (in grams).

    Methods:
        run(): Executes the pouring process, transferring content from the source to the destination at the specified rate.

    Example Usage:
        source = Recipient(name="Source Bowl")
        destination = Recipient(name="Destination Bowl")
        verseur = Verseur(name="Pourer", source=source, destination=destination, rate=10, target_quantity=370)
        verseur.start()
        verseur.join()
    """

    def __init__(self, name: str, source, destination, rate: int, target_quantity: float):
        """
        Initializes a new instance of the Verseur class.

        Args:
            name (str): The name of the verseur.
            source (Recipient): The source container to pour from.
            destination (Recipient): The destination container to pour into.
            rate (int): The rate at which content is poured per second (in grams).
            target_quantity (float): The total quantity of content to be poured (in grams).
        """
        super().__init__()
        self.name = name
        self.source = source
        self.destination = destination
        self.rate = rate
        self.target_quantity = target_quantity

    def run(self):
        """
        Executes the pouring process.

        This method repeatedly pours content from the source container to the destination container at the specified rate
        until the target quantity is reached. It ensures that the pouring is thread-safe and that 30 grams of content
        remains in the source container after the pouring is complete.

        The method:
        - Acquires the lock for the source container to ensure thread-safe access.
        - Pours the content in batches according to the specified rate.
        - Updates the quantities of the content and ensures that the source container retains 30 grams of content if needed.
        - Prints messages indicating the amount of content being poured and the status of the operation.

        The method also simulates a delay between each pouring operation to represent the time taken for pouring.
        """
        total_poured = 0
        while total_poured < self.target_quantity:
            with self.source.lock:
                if not self.source.content or self.source.content[0].quantity <= 0:
                    break
                item = self.source.content[0]
                quantity_to_pour = min(self.rate, item.quantity)
                if total_poured + quantity_to_pour > self.target_quantity:
                    quantity_to_pour = self.target_quantity - total_poured

                item.quantity -= quantity_to_pour
                total_poured += quantity_to_pour

                if item.quantity == 0:
                    self.source.content.pop(0)
                self.destination.ajouter_content(Chocolat(quantity=quantity_to_pour))

            print(f"{self.name} pours {quantity_to_pour} grams of chocolate into {self.destination.name}")
            time.sleep(1)  # Wait for 1 second before pouring the next batch

        # Ensure 30 grams of chocolate remains in the source
        with self.source.lock:
            if self.source.content and self.source.content[0].quantity > 30:
                remaining_chocolate = self.source.content[0].quantity - 30
                self.source.content[0].quantity = 30
                self.source.ajouter_content(Chocolat(quantity=remaining_chocolate))

        print(f"{self.name} has finished pouring the content.")
