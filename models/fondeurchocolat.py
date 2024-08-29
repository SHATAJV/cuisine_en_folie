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
        """
        Initializes a new instance of the FondeurChocolat class.

        Args:
            name (str): The name of the chocolate melter.
            quantity (float): The quantity of chocolate to be melted, in grams.
        """
        threading.Thread.__init__(self)
        self.name = name
        self.quantity = quantity

    def run(self):
        """
        Executes the chocolate melting process.

        This method simulates the process of heating water, pouring it into a pan,
        placing a bowl of chocolate, and then melting the chocolate by stirring it in
        multiple rounds. Each round is calculated based on a fixed quantity of chocolate
        to be melted per round.

        The process includes:
        - Heating water in a kettle.
        - Pouring the water into a pan.
        - Placing a bowl filled with chocolate.
        - Melting the chocolate in rounds.
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
