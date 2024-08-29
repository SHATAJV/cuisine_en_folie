import threading
import time
from models.commis import Commis

class Verseur(Commis):
    def __init__(self, name: str, source, destination, rate: int):
        super().__init__(name)
        self.source = source
        self.destination = destination
        self.rate = rate

    def run(self):
        while self.source.content and self.source.content[0].quantity > 0:
            item = self.source.content[0]
            quantity_to_verser = min(self.rate, item.quantity)
            print(f"{self.name} verse {quantity_to_verser} {item.unit} de {item.name} dans {self.destination.name}")
            item.quantity -= quantity_to_verser
            if item.quantity == 0:
                with self.source.lock:
                    self.source.content.pop(0)
            self.destination.ajouter_content(item)
            time.sleep(1)
        print(f"{self.name} a terminé de verser le contenu.")
