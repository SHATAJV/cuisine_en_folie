import threading

from models.appareil import Appareil
from models.battre_ouf import BatteurOeufs
from models.fondeurchocolat import FondeurChocolat
from models.recipient import Recipient
from models.verseur import Verseur


def main():
    # Création des objets
    recipient_oeufs = Recipient(name="bol d'œufs")
    recipient_chocolat = Recipient(name="bol de chocolat")

    # Création des commis
    fondeur_1 = FondeurChocolat(name="Fondeur 1", quantity=200, recipient=recipient_chocolat)
    batteur_1 = BatteurOeufs(name="Batteur 1", nb_oeufs=6, recipient=recipient_oeufs)

    # Démarrer les threads pour le fondeur de chocolat et le batteur d'œufs
    fondeur_1.start()

    batteur_1.start()

    # Attendre la fin des threads
    fondeur_1.join()

    batteur_1.join()

    # Afficher le contenu des récipients après les tâches des commis
    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()

    # Verrou pour la gestion des versements simultanés
    lock = threading.Lock()

    # Création et démarrage des verseurs
    verseur1 = Verseur(name="Verseur 1", source=recipient_chocolat, destination=recipient_oeufs, rate=10, lock=lock)
    verseur2 = Verseur(name="Verseur 2", source=recipient_chocolat, destination=recipient_oeufs, rate=10, lock=lock)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    # Afficher le contenu des récipients après le versement
    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()

    # Utilisation de l'appareil
    appareil = Appareil()
    appareil.ajouter_ingredient(recipient_chocolat.content)
    appareil.ajouter_ingredient(recipient_oeufs.content)
    appareil.melanger()

if __name__ == "__main__":
    main()
