# Rapport

-Implémentation de la méthode connexe() pour vérifier si le graphe est connexe. Cela est important pour déterminer s'il existe une chaîne eulérienne possible. Si le graphe n'est pas connexe, il n'y a pas de chaîne eulérienne.

-Implémentation de la méthode eulerien() pour vérifier si le graphe est eulérien ou semi-eulérien. Cette méthode parcourt les sommets du graphe et compte le nombre de sommets de degré impair. Si le graphe est eulérien, la méthode renvoie 0. Sinon, elle renvoie le sommet de degré impair (si le graphe est semi-eulérien) ou le nombre total de sommets (si le graphe n'est pas semi-eulérien).

-Dans la méthode chaine_eulerienne_poids_min(), j’ai utilisé l'algorithme de Hierholzer modifié pour trouver une chaîne eulérienne dans le graphe. Si le graphe n'est pas connexe, la méthode renvoie une liste vide. Si le graphe n'est pas eulérien, la méthode renvoie également une liste vide. Si le graphe est eulérien ou semi eulérien la méthode calcule la distance totale de la chaîne eulérienne en ajoutant les poids des arêtes parcourues.


-Une méthode get_edge_weight(u, v) pour obtenir le poids d'une arête donnée entre deux sommets.

-Implémentation de la méthode ajouter_arretes_artificielles() pour ajouter des arêtes artificielles entre les sommets de degré impair, afin de rendre le graphe eulérien. Cela garantit qu'il existe une chaîne eulérienne dans le graphe modifié.

-La méthode ajouter_arretes_artificielles() est utilisée dans le cas où le graphe n’est eulérien, cela permet de le rendre eulérien et de trouver par la suite  une chaîne pseudo-eulérienne en parcourant les arêtes qui existaient dans  graphe initialement et en ignorant dans le parcours eulérien les arêtes artificielles, mais je n’ai pas pu trouver pour l’instant une méthode qui utilise cette technique tout en gardant le parcours eulérien connexe et optimale en terme de coût. L’idée que j’ai eue était de remplacer les arêtes artificielles entre deux sommets u et v par la chaîne calculée par l’algorithme de dijkstra, mais cela, à mon humble opinion ne garantit pas l’optimalité globale du parcours pseudo-eulérien et peut utiliser plusieurs fois les mêmes arêtes dans le parcours.
