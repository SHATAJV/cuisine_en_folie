import threading

class Recipient:
    """
    A class representing a recipient that can hold and manage content with thread-safe operations.

    The `Recipient` class is used to manage items that are added to or retrieved from a container.
    It supports concurrent access through the use of a lock to ensure thread safety when modifying
    or accessing the content.

    Attributes:
        name (str): The name of the recipient, typically representing the container's name.
        content (list): A list holding the items currently in the recipient. Defaults to an empty list.
        lock (threading.Lock): A lock to manage concurrent access to the content.

    Methods:
        ajouter_content(item): Adds an item to the recipient's content list in a thread-safe manner.
        afficher_contenu(): Displays the content of the recipient in a thread-safe manner.

    Example Usage:
        recipient = Recipient(name="Bowl")
        recipient.ajouter_content(item)
        recipient.afficher_contenu()
    """

    def __init__(self, name: str, content=None):
        """
        Initializes a new instance of the Recipient class.

        Args:
            name (str): The name of the recipient.
            content (list, optional): The initial content to be added to the recipient. Defaults to an empty list.
        """
        self.name = name
        self.content = content if content is not None else []
        self.lock = threading.Lock()

    def ajouter_content(self, item):
        """
        Adds an item to the recipient's content list.

        This method acquires a lock to ensure that the addition of the item to the content list
        is thread-safe. It prints a message indicating the quantity and name of the item being added.

        Args:
            item (object): The item to be added. The item should have `name` and `quantity` attributes.
        """
        with self.lock:
            print(f"Adding {item.quantity} grams of {item.name} to {self.name}")
            self.content.append(item)

    def afficher_contenu(self):
        """
        Displays the content of the recipient.

        This method acquires a lock to ensure that the content retrieval is thread-safe. It prints
        a message showing the list of contained items or indicating that the recipient is empty.

        If the recipient has content, each item is converted to a string representation and listed.

        If no content is present, a message indicating that the recipient is empty is printed.
        """
        with self.lock:
            if not self.content:
                print(f"{self.name} is empty.")
            else:
                print(f"{self.name} contains: {', '.join(str(c) for c in self.content)}")
