from abc import ABC, abstractmethod


class Commis(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

