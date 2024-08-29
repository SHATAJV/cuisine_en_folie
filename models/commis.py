from abc import ABC, abstractmethod
import threading

class Commis(ABC, threading.Thread):
    """
    An abstract base class representing a commis (a type of assistant or worker)
    that extends threading.Thread to support concurrent execution.

    Attributes:
        name (str): The name of the commis.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of the Commis class.

        Args:
            name (str): The name of the commis.
        """
        threading.Thread.__init__(self)
        self.name = name

    @abstractmethod
    def run(self):
        """
        Abstract method that should be implemented by subclasses.

        This method contains the code that defines the task the commis will perform
        when the thread is started. Each subclass should provide its own implementation.
        """
        pass
