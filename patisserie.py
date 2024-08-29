import threading

from models.appareil import Appareil
from models.battre_ouf import BatteurOeufs
from models.fondeurchocolat import FondeurChocolat
from models.recipient import Recipient
from models.verseur import Verseur


def main():

    recipient_oeufs = Recipient(name="bol d'œufs")
    recipient_chocolat = Recipient(name="bol de chocolat")

    fondeur_1 = FondeurChocolat(name="Fondeur 1", quantity=200, recipient=recipient_chocolat)
    fondeur_2 = FondeurChocolat(name="Fondeur 2", quantity=200, recipient=recipient_chocolat)
    batteur_1 = BatteurOeufs(name="Batteur 1", nb_oeufs=6, recipient=recipient_oeufs)

    fondeur_1.start()
    fondeur_2.start()
    batteur_1.start()

    fondeur_1.join()
    fondeur_2.join()
    batteur_1.join()


    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()


    lock = threading.Lock()


    verseur1 = Verseur(name="Verseur 1", source=recipient_chocolat, destination=recipient_oeufs, rate=10, lock=lock)
    verseur2 = Verseur(name="Verseur 2", source=recipient_chocolat, destination=recipient_oeufs, rate=10, lock=lock)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()


    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()


    appareil = Appareil()
    appareil.ajouter_ingredient(recipient_chocolat.content)
    appareil.ajouter_ingredient(recipient_oeufs.content)
    appareil.melanger()


if __name__ == "__main__":
    main()
