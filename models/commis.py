from abc import ABC, abstractmethod
import threading

# Classe abstraite Commis avec threading
class Commis(ABC, threading.Thread):
    def __init__(self, name):
        # Appeler explicitement le constructeur de threading.Thread
        threading.Thread.__init__(self)
        self.name = name

    @abstractmethod
    def run(self):
        pass
