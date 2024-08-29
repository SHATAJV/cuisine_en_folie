from models.ingrediants import Ingredient
import threading
import time
import math

class Chocolat:
    def __init__(self, quantity):
        self.name = "Chocolat"
        self.quantity = quantity
        self.fondeur_thread = None

    def fondre(self):

        if not self.fondeur_thread:
            self.fondeur_thread = threading.Thread(target=self.fondrechocolat)
            self.fondeur_thread.start()
        else:
            print("Le chocolat est déjà en train de fondre.")

    def fondrechocolat(self):

        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)
        nb_tours = math.ceil(self.quantity / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"Je mélange {self.quantity} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)
