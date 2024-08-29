from abc import ABC, abstractmethod

class Commis(ABC):
    """
    Abstract base class representing a kitchen assistant.

    Attributes:
        name (str): The name of the kitchen assistant.
    """

    def __init__(self, name: str):
        """
        Initializes the Commis with a given name.

        Args:
            name (str): The name of the kitchen assistant.
        """
        self.name = name

    @abstractmethod
    def work(self):
        """
        Abstract method that must be implemented by subclasses.

        This method should define the specific tasks or actions
        that the kitchen assistant performs.
        """
        pass
