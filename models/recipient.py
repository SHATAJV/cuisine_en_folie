import threading


class Recipient:
    """
    A class representing a recipient that can hold and manage content.

    Attributes:
        name (str): The name of the recipient.
        content (list): The list of items currently held by the recipient.
        lock (threading.Lock): A lock to manage concurrent access to the content.
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

        Args:
            item (object): The item to be added. The item may have a `name` attribute,
                           or it can be a simple value.

        Prints a message indicating the addition of the item to the recipient.
        """
        with self.lock:
            if hasattr(item, 'name'):
                print(f"Adding {item.name} to {self.name}")
            else:
                print(f"Adding {item} to {self.name}")
            self.content.append(item)

    def afficher_contenu(self):
        """
        Displays the content of the recipient.

        Prints a message indicating whether the recipient is empty or shows the list of contained items.
        """
        with self.lock:
            if not self.content:
                print(f"{self.name} is empty.")
            else:
                print(f"{self.name} contains: {', '.join(str(c) for c in self.content)}")
