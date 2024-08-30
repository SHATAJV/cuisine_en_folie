import threading

class Recipient:
    def __init__(self, name: str, content=None):
        self.name = name
        self.content = content if content is not None else []
        self.lock = threading.Lock()

    def ajouter_content(self, item):
        with self.lock:
            print(f"Adding {item.quantity} grams of {item.name} to {self.name}")
            self.content.append(item)

    def afficher_contenu(self):
        with self.lock:
            if not self.content:
                print(f"{self.name} is empty.")
            else:
                print(f"{self.name} contains: {', '.join(str(c) for c in self.content)}")
