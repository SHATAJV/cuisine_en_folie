import threading
import time


class Batteur(threading.Thread):
    """
    A class representing a thread that simulates beating eggs.

    The `Batteur` class extends `threading.Thread` and is used to simulate the process
    of beating a specified quantity of eggs in multiple rounds. This class models
    the concurrent execution of this task, making use of threading.

    Attributes:
        name (str): The name of the batteur (beater) thread.
        quantity (int): The number of eggs to be beaten.

    Methods:
        run(): Executes the process of beating the eggs in multiple rounds. Each round
               simulates a period of time during which the eggs are beaten.

    Example Usage:
        batteur = Batteur(name="Egg Beater", quantity=6)
        batteur.start()  # Start the thread
        batteur.join()   # Wait for the thread to finish
    """

    def __init__(self, name: str, quantity: int):
        """
        Initializes a new instance of the Batteur class.

        Args:
            name (str): The name of the batteur thread.
            quantity (int): The number of eggs to be beaten.
        """
        super().__init__()
        self.name = name
        self.quantity = quantity

    def run(self):
        """
        Executes the process of beating the eggs.

        This method simulates the process of beating a specified number of eggs in
        multiple rounds. It prints messages indicating the start, progress, and end
        of the beating process. Each round of beating is simulated with a sleep delay
        to represent the time taken for each round.

        The process includes:
        - Printing a message indicating the start of beating the eggs.
        - Simulating the beating process in 6 rounds with a 1-second delay per round.
        - Printing a message indicating the completion of the beating process.
        """
        print(f"{self.name} starts beating {self.quantity} eggs.")
        # Simulate beating eggs in rounds
        for round_number in range(1, 7):
            print(f"{self.name} is beating the eggs, round #{round_number}")
            time.sleep(1)  # Simulate time taken for each round
        print(f"{self.name} has finished beating the eggs.")
