import time

from models.commis import Commis
from models.oeuf import Oeuf


class BatteurOeufs(Commis):
    def __init__(self, name, nb_oeufs, recipient):
        super().__init__(name)  # Appelle le constructeur de la classe mère `Commis`
        self.nb_oeufs = nb_oeufs
        self.recipient = recipient

    def run(self):
        print(f"{self.name} bats les {self.nb_oeufs} oeufs.")
        for i in range(1, self.nb_oeufs + 1):
            print(f"{self.name} est en train de battre l'œuf n°{i}.")
            time.sleep(1)
        print(f"{self.name} a terminé de battre les œufs.")
        self.recipient.ajouter_content(Oeuf(self.nb_oeufs))
