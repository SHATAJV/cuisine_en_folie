import threading
import time


class Verseur(threading.Thread):
    def __init__(self, name, source, destination, rate):
        threading.Thread.__init__(self)
        self.name = name
        self.source = source
        self.destination = destination
        self.rate = rate

    def run(self):
        while self.source.content and self.destination:
            print(f"{self.name} verse de {self.source.name} à {self.destination.name}.")

            time.sleep(self.rate)
            
