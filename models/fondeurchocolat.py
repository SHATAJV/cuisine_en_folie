import threading
import time
import math


class FondeurChocolat(threading.Thread):
    """
    A class representing a chocolate melter that extends threading.Thread to perform
    tasks concurrently.

    Attributes:
        name (str): The name of the chocolate melter.
        quantity (float): The quantity of chocolate to be melted, in grams.
    """

    def __init__(self, name: str, quantity: float):
        super().__init__()
        self.name = name
        self.quantity = quantity
        self.lock = threading.Lock()

    def run(self):
        """
        Executes the chocolate melting process.
        """
        print(f"{self.name} puts water to heat in a kettle")
        time.sleep(8)
        print(f"{self.name} pours the water into a pan")
        time.sleep(2)
        print(f"{self.name} places the bowl filled with chocolate")
        time.sleep(1)

        # Calculate the number of stirring rounds needed based on the quantity
        nb_tours = math.ceil(self.quantity / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.name} stirs {self.quantity} grams of chocolate, round #{no_tour}")
            time.sleep(1)