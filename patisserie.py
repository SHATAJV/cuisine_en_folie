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
    recipent_chocolat = Recipient(name="bol de chocolat")
    recipent_oeufs = Recipient(name="bol d'œufs", content=oeuf)

    # Création des fondeurs de chocolat
    commis_1 = FondeurChocolat(name="Fondeur 1", quantity=200)
    commis_2 = BatteurOeufs(name="Batteur 1", nb_oeufs=6)

    # Création des verseurs
    verseur1 = Verseur(name="Verseur 1", source=recipent_chocolat, destination=recipent_oeufs, rate=10)

    # Démarrer les threads pour le fondeur et le batteur
    commis_1.start()
    commis_2.start()

    # Assurer que le fondeur et le batteur ont terminé avant de commencer le verseur
    commis_1.join()
    commis_2.join()

    # Mettre le chocolat fondu dans le récipient
    recipent_chocolat.content = chocolat

    # Démarrer le verseur
    verseur1.start()
    verseur1.join()

    # Afficher le contenu des récipients après le versement
    recipent_chocolat.afficher_contenu()
    recipent_oeufs.afficher_contenu()

    # Utilisation de l'appareil
    appareil = Appareil()
    appareil.ajouter_ingredient(chocolat)
    appareil.ajouter_ingredient(oeuf)
    appareil.melanger()

if __name__ == "__main__":
    main()
