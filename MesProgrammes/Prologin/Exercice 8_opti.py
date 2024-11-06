from typing import List

def desequilibre_minimal(n: int, k: int, barres: List[int]) -> None:
    """
    Affiche le déséquilibre minimal possible pour construire un échafaudage de K étages.
    
    :param n: le nombre de barres
    :param k: le nombre d'étages à construire
    :param barres: une liste des tailles des barres
    """
    # Trier les barres par tailles croissantes
    barres.sort()

    # Liste des déséquilibres entre chaque paire consécutive
    differences = [(barres[i+1] - barres[i], i, i+1) for i in range(n - 1)]
    
    # Trier les différences par ordre croissant
    differences.sort()

    # Sélectionner les K paires avec les plus petites différences sans conflit d'indices
    used_indices = set()
    selected_desequilibres = []
    
    for diff, i, j in differences:
        if i not in used_indices and j not in used_indices:
            selected_desequilibres.append(diff)
            used_indices.add(i)
            used_indices.add(j)
            # Vérifier si on a atteint le nombre requis de paires
            if len(selected_desequilibres) == k:
                break
    
    # Calculer le déséquilibre total minimal
    desequilibre_min = sum(selected_desequilibres)
    
    # Afficher le résultat
    print(desequilibre_min)

# Exemple d'utilisation :
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    barres = list(map(int, input().split()))
    desequilibre_minimal(n, k, barres)
