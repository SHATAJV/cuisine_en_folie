import threading


class Oeufs(threading.Thread):
    def __init__(self, nb_oeufs):
        threading.Thread.__init__(self)
        self.nb_oeufs = nb_oeufs

    def use(self):
        print(f"Utilisation des {self.quantity} oeufs.")