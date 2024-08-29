from abc import ABC, abstractmethod
import threading

class Commis(ABC, threading.Thread):
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.name = name

    @abstractmethod
    def run(self):
        pass
