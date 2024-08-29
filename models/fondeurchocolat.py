from models.commis import Commis


import threading
import time
import math

class FondeurChocolat(threading.Thread):
    def __init__(self, name, quantity):
        threading.Thread.__init__(self)
        self.name = name
        self.quantity = quantity

    def run(self):
        print(f"{self.name} met de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print(f"{self.name} verse l'eau dans une casserole")
        time.sleep(2)
        print(f"{self.name} pose le bol rempli de chocolat")
        time.sleep(1)
        nb_tours = math.ceil(self.quantity / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.name} mélange {self.quantity} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)
