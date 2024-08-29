•
ajouter un nom à chaque classe de thread représentant un commis (dans une classe abstraite)
•
introduire une classe abstraite Ingredient (nom, quantité, unité) et deux classes filles Oeuf et Chocolat
•
introduire une classe Appareil pour modéliser un « mélange homogène de plusieurs ingrédients et utilisé comme base pour un gâteau, une tarte, une glace, … avant sa cuisson ou son turbinage. »
•
introduire une classe Recipient (ex. cul de poule: « récipient généralement en inox et forme de saladier et fond arrondi utilisé pour toutes les préparations à mélanger. »), contenant un ingrédient ou un appareil qui est travaillé ; un objet de cette classe est passé au constructeur d'un commis permettant de préciser le récipient avec lequel il effectue son action
•
ajouter un second commis fondeur de chocolat
•
introduire une classe de commis Verseur, chargé de verser à un certain rythme le contenu d'un récipient dans celui d'un autre
•
les deux fondeurs de chocolat, une fois leur tâche réalisée, laissent la place à deux verseurs qui utilisent simultanément leur récipient, pour verser petit à petit leur chocolat dans le récipient contenant les oeufs
•
trouver une granularité de temps faisant apparaitre une condition critique lors de ces deux actions simultanées
•
introduire un verrou pour la résoudre
