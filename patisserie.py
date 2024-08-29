from models.battre_ouf import BatteurOeufs
from models.chocolat import Chocolat
from models.oeuf import Oeuf
from models.fondeurchocolat import FondeurChocolat
from models.recipient import Recipient
from models.verseur import Verseur
from models.appareil import Appareil


def main():
    # Création des objets
    oeuf = Oeuf(quantity=6)
    chocolat = Chocolat(quantity=200)

    # Création des récipients
    recipent_chocolat = Recipient(name="bol de chocolat", content=chocolat)
    recipent_oeufs = Recipient(name="bol d'œufs", content=oeuf)

    # Création des fondeurs de chocolat
    Commis_1 = FondeurChocolat(name="Fondeur 1", quantity=200)
    commis_2= BatteurOeufs(name="Batteur 1", quantity=6)
  

    # Création des verseurs
    verseur1 = Verseur(name="Verseur 1", source=recipent_chocolat, destination=recipent_oeufs, rate=1)
    verseur2 = Verseur(name="Verseur 2", source=recipent_chocolat, destination=recipent_oeufs, rate=1)

    # Démarrer les threads
    Commis_1.start()
    commis_2.start()

    Commis_1.join()
    commis_2.join()


    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    # Afficher le contenu des récipients
    recipent_chocolat.afficher_contenu()
    recipent_oeufs.afficher_contenu()

    # Utilisation de l'appareil
    appareil = Appareil()
    appareil.ajouter_ingredient(chocolat)
    appareil.ajouter_ingredient(oeuf)
    appareil.melanger()


if __name__ == "__main__":
    main()
