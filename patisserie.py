from models.recipient import Recipient
from models.oeuf import Oeuf
from models.chocolat import Chocolat
from models.fondeurchocolat import FondeurChocolat
from models.battre_ouf import Batteur
from models.verseur import Verseur
from models.appareil import Appareil


def main():
    """
    main() function for preparing chocolate mousse.

    This function simulates the process of making chocolate mousse by coordinating various tasks using threads.
    It performs the following steps:

    1. **Create Recipients:**
       - Initializes two `Recipient` objects: one for holding melted chocolate (`bol_chocolat`) and one for holding the beaten eggs and chocolate mixture (`bol_oeufs`).

    2. **Start Beating Eggs:**
       - Creates a `Batteur` thread to beat 6 eggs and starts it.

    3. **Start Melting Chocolate:**
       - Creates two `FondeurChocolat` threads, each responsible for melting 200 grams of chocolate, and starts them.

    4. **Combine Melted Chocolate:**
       - Waits for the `FondeurChocolat` threads to finish melting the chocolate.
       - Combines the melted chocolate from both `FondeurChocolat` threads into `bol_chocolat`, totaling 400 grams.

    5. **Add Beaten Eggs:**
       - Waits for the `Batteur` thread to finish beating the eggs.
       - Adds the beaten eggs to `bol_oeufs`.

    6. **Pour Chocolate into Eggs:**
       - Creates a `Verseur` thread to pour 370 grams of melted chocolate into `bol_oeufs` in increments of 10 grams, leaving 30 grams in `bol_chocolat`.
       - Starts and waits for the `Verseur` thread to complete the pouring process.

    7. **Display Final Contents:**
       - Prints the final contents of `bol_oeufs` and `bol_chocolat`.
       - Displays the quantities of eggs and chocolate used.

    8. **Mix Ingredients:**
       - Prints the list of ingredients mixed together for the final chocolate mousse.

    9. **Final Message:**
       - Displays a message indicating that the chocolate mousse is ready.

    This function demonstrates multithreading and coordination of different processes in a recipe preparation workflow.

    """

    # Create recipients
    bol_chocolat = Recipient(name="Bol de chocolat")
    bol_oeufs = Recipient(name="Bol d'œufs")

    # Create and start Batteur thread to beat eggs
    batteur = Batteur(name="Batteur Oeufs", quantity=6)
    batteur.start()

    # Create and start Fondeur threads to melt chocolate
    fondeur1 = FondeurChocolat(name="Fondeur 1", quantity=200)
    fondeur2 = FondeurChocolat(name="Fondeur 2", quantity=200)
    fondeur1.start()
    fondeur2.start()

    # Wait for fondeur threads to finish melting
    fondeur1.join()
    fondeur2.join()

    # Combine melted chocolate
    bol_chocolat.ajouter_content(Chocolat(quantity=200))  # Fondeur 1
    bol_chocolat.ajouter_content(Chocolat(quantity=200))  # Fondeur 2

    print(f"Bol de chocolat contains: 400 grams Chocolat fondu")

    # Wait for batteur to finish beating eggs
    batteur.join()

    # Add beaten eggs to bol d'œufs
    oeufs = Oeuf(quantity=6)
    bol_oeufs.ajouter_content(oeufs)

    # Create and start Verseur thread to pour chocolate into bol d'œufs
    verseur = Verseur(name="Verseur", source=bol_chocolat, destination=bol_oeufs, rate=10, target_quantity=370)
    verseur.start()

    # Wait for verseur to finish pouring
    verseur.join()

    # Print the final contents of bol d'œufs and bol de chocolat
    bol_oeufs.afficher_contenu()
    if bol_chocolat.content:
        print(f"Bol de chocolat contains: {bol_chocolat.content[0].quantity} grams Chocolat")
    else:
        print("Bol de chocolat is empty.")

    # Mixing ingredients
    print("Mixing ingredients:")
    print(f"- {oeufs.quantity} number of Oeuf")
    print(f"- {370} grams Chocolat")

    # Final message
    print("Votre mousse au chocolat est prête!")

if __name__ == "__main__":
    main()
