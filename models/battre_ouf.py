import threading
import time
from models.commis import Commis
from models.oeuf import Oeuf

class BatteurOeufs(Commis):
    def __init__(self, name: str, nb_oeufs: int, recipient):
        super().__init__(name)
        self.nb_oeufs = nb_oeufs
        self.recipient = recipient

    def run(self):
        print(f"{self.name} commence à battre {self.nb_oeufs} œufs.")
        for i in range(self.nb_oeufs):
            print(f"{self.name} bat les œufs, tour n°{i + 1}")
            time.sleep(1)
        beaten_eggs = Oeuf(quantity=self.nb_oeufs)
        self.recipient.ajouter_content(beaten_eggs)
        print(f"{self.name} a terminé de battre les œufs.")
