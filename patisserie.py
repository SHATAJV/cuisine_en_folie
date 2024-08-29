from models.recipient import Recipient
from models.oeuf import Oeuf
from models.chocolat import Chocolat
from models.fondeurchocolat import FondeurChocolat
from models.battre_ouf import BatteurOeufs
from models.verseur import Verseur
from models.appareil import Appareil

def main():
    recipient_oeufs = Recipient(name="bol d'œufs")
    recipient_chocolat = Recipient(name="bol de chocolat", content=[Chocolat(quantity=200)])

    fondeur_1 = FondeurChocolat(name="John", quantity=200)
    batteur_1 = BatteurOeufs(name="Emilie", nb_oeufs=6, recipient=recipient_oeufs)

    fondeur_1.start()
    batteur_1.start()

    fondeur_1.join()
    batteur_1.join()

    verseur1 = Verseur(name="Verseur 1", source=recipient_chocolat, destination=recipient_oeufs, rate=10)
    verseur2 = Verseur(name="Verseur 2", source=recipient_chocolat, destination=recipient_oeufs, rate=10)

    verseur1.start()
    verseur2.start()

    verseur1.join()
    verseur2.join()

    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()

    appareil = Appareil()
    if recipient_chocolat.content:
        appareil.ajouter_ingredient(recipient_chocolat.content[0])
    if recipient_oeufs.content:
        appareil.ajouter_ingredient(recipient_oeufs.content[0])
    appareil.melanger()


if __name__ == "__main__":
    main()
