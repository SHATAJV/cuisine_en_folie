import threading
import time
import math

class FondeurChocolat(threading.Thread):
    """
    Represents a chocolate melter that performs tasks in a separate thread.

    Inherits from:
        threading.Thread: The base class for running threads.

    Attributes:
        name (str): The name of the chocolate melter.
        quantity (float): The amount of chocolate to be melted, in grams.
    """

    def __init__(self, name: str, quantity: float):
        """
        Initializes the FondeurChocolat with a name and quantity of chocolate.

        Args:
            name (str): The name of the chocolate melter.
            quantity (float): The amount of chocolate to be melted, in grams.
        """
        threading.Thread.__init__(self)
        self.name = name
        self.quantity = quantity

    def run(self):
        """
        Executes the tasks of melting chocolate in a separate thread.

        Steps performed:
            1. Heats water in a kettle.
            2. Pours the hot water into a pan.
            3. Places a bowl filled with chocolate on the pan.
            4. Stirs the chocolate in the bowl, performing multiple stirs based on the quantity.

        Outputs:
            Prints the progress and actions performed during the chocolate melting process.
        """
        print(f"{self.name} met de l'eau à chauffer dans une bouilloire")
        time.sleep(8)  # Simulates the time for heating water
        print(f"{self.name} verse l'eau dans une casserole")
        time.sleep(2)  # Simulates the time for pouring water into a pan
        print(f"{self.name} pose le bol rempli de chocolat")
        time.sleep(1)  # Simulates the time for placing the bowl
        nb_tours = math.ceil(self.quantity / 10)  # Number of stirs needed based on the quantity
        for no_tour in range(1, nb_tours + 1):
            print(f"{self.name} mélange {self.quantity} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)  # Simulates the time for each stir
