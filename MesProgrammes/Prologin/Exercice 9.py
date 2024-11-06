from typing import List
from itertools import permutations

def meilleure_muraille(n: int, sortie: List[int], entree: List[int]) -> None:
    """
    Calcule et affiche le coût minimal d'un cycle passant par toutes les tours
    ainsi que l'ordre des tours visitées.
    
    :param n: Le nombre de tours
    :param sortie: Liste des profondeurs des portes de sortie de chaque tour
    :param entree: Liste des profondeurs des portes d'entrée de chaque tour
    """
    # On démarre toujours à la Tour 0, calcul du coût initial de référence
    permut_cycle_min = range(1, n)
    Ti = 0
    cout_cycle_min = 0
    for Tj in permut_cycle_min:
        cout_cycle_min += (sortie[Ti] - entree[Tj]) ** 2
        Ti = Tj
    # Ajout du coût pour revenir de la dernière tour à la première
    cout_cycle_min += (sortie[Ti] - entree[0]) ** 2

    # Parcours de toutes les permutations possibles des tours, sauf la tour de départ
    tours_permutations_list = permutations(range(1, n))
    for permut in tours_permutations_list:
        Ti = 0
        cout_cycle = 0
        for Tj in permut:
            cout_cycle += (sortie[Ti] - entree[Tj]) ** 2
            # Arrêt précoce si le coût actuel dépasse le minimum enregistré
            if cout_cycle >= cout_cycle_min:
                break
            Ti = Tj
        # Ajouter le coût de retour à la première tour
        cout_cycle += (sortie[Ti] - entree[0]) ** 2
        # Mise à jour si un coût plus faible est trouvé
        if cout_cycle < cout_cycle_min:
            cout_cycle_min = cout_cycle
            permut_cycle_min = permut

    # Affichage du coût minimal et de l'ordre optimal des tours
    print(cout_cycle_min)
    # Affiche la séquence optimale de visites en commençant et terminant à 0
    print("0", end=" ")
    for t in permut_cycle_min:
        print(t, end=" ")
    print("0")

# Exemple d'utilisation
if __name__ == "__main__":
    n = int(input())
    sortie = list(map(int, input().split()))
    entree = list(map(int, input().split()))

    meilleure_muraille(n, sortie, entree)
