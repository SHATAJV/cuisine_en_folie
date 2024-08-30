
import threading
from models.chocolat import Chocolat
from models.commis import Commis
import time


class Verseur(threading.Thread):
    def __init__(self, name: str, source, destination, rate: int, target_quantity: float):
        super().__init__()
        self.name = name
        self.source = source
        self.destination = destination
        self.rate = rate
        self.target_quantity = target_quantity

    def run(self):
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
