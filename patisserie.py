from models.recipient import Recipient
from models.oeuf import Oeuf
from models.chocolat import Chocolat
from models.fondeurchocolat import FondeurChocolat
from models.battre_ouf import BatteurOeufs
from models.verseur import Verseur
from models.appareil import Appareil

def main():
    # Création des récipients pour les œufs et le chocolat
    recipient_oeufs = Recipient(name="bol d'œufs")
    recipient_chocolat = Recipient(name="bol de chocolat", content=[Chocolat(quantity=200)])

    # Initialisation des threads pour fondre le chocolat et battre les œufs
    fondeur_1 = FondeurChocolat(name="John", quantity=200)
    batteur_1 = BatteurOeufs(name="Emilie", nb_oeufs=6, recipient=recipient_oeufs)

    # Démarrage des threads
    fondeur_1.start()
    batteur_1.start()

    # Attente de la fin des threads
    fondeur_1.join()
    batteur_1.join()

    # Variables pour gérer la quantité de chocolat à verser
    total_chocolat_a_verser = 170
    chocolat_restant = recipient_chocolat.content[0].quantity - total_chocolat_a_verser

    # Versement de 170g de chocolat dans le bol d'œufs
    recipient_oeufs.ajouter_content(Chocolat(quantity=total_chocolat_a_verser))
    recipient_chocolat.content[0].quantity = chocolat_restant

    # Affichage du contenu des récipients
    recipient_chocolat.afficher_contenu()
    recipient_oeufs.afficher_contenu()

    # Mélange des ingrédients dans l'appareil
    appareil = Appareil()
    for ingredient in recipient_oeufs.content:
        appareil.ajouter_ingredient(ingredient)
    appareil.melanger()

    # Message final
    print("Votre mousse au chocolat est prête!")

if __name__ == "__main__":
    main()
