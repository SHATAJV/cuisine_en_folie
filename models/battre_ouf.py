from models.commis import Commis


class BatteurOeufs(Commis):
    def __init__(self, name, nb_oeufs):
        super().__init__(name)
        self.nb_oeufs = nb_oeufs

    def work(self):
        print(f"{self.name} bats les {self.nb_oeufs} oeufs.")
