import threading
import time


class Batteur(threading.Thread):
    def __init__(self, name: str, quantity: int):
        super().__init__()
        self.name = name
        self.quantity = quantity

    def run(self):
        print(f"{self.name} starts beating {self.quantity} eggs.")
        # Simulate beating eggs in rounds
        for round_number in range(1, 7):
            print(f"{self.name} is beating the eggs, round #{round_number}")
            time.sleep(1)  # Simulate time taken for each round
        print(f"{self.name} has finished beating the eggs.")
