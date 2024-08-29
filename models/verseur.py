import threading
import time

import time

from models.commis import Commis


class Verseur(Commis):
    def __init__(self, name, source, destination, rate):
        super().__init__(name)
        self.source = source
        self.destination = destination
        self.rate = rate

    def work(self):
        global lock
        with lock:
            quantity_to_verser = self.source.content.quantity
            while quantity_to_verser > 0:
                amount_to_verse = min(self.rate, quantity_to_verser)
                print(f"{self.name} verse {amount_to_verse} grammes du {self.source.name} dans le {self.destination.name}")
                quantity_to_verser -= amount_to_verse
                time.sleep(1)
            print(f"{self.name} a terminé de verser le contenu.")

