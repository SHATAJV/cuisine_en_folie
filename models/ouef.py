import threading
import time

class Oeuf:
    def __init__(self, quantity):
        self.name = "Oeuf"
        self.quantity = quantity
        self.batteur_thread = None

    def battre(self):

        if not self.batteur_thread:
            self.batteur_thread = threading.Thread(target=self.battreouef)
            self.batteur_thread.start()
        else:
            print("Les oeufs sont déjà en cours de battage.")

    def battreouef(self):

        nb_tours = self.quantity * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.quantity} oeufs, tour n°{no_tour}")
            time.sleep(0.5)
