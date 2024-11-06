from typing import List

def desequilibre_minimal(n: int, k: int, barres: List[int]) -> None:
    """
    :param n: le nombre de barres
    :param k: le nombre d'étages à construire
    :param barres: la taille des barres
    """
    # TODO Afficher, sur une ligne, le déséquilibre minimal possible pour
    # construire son échaufadage.

    # Trier le tableau barres par longueurs croissantes
    barres.sort()

    # Création liste de déséquilibres 2 à 2
    # element=[indice, desequilibre]
    desequilibres = []
    for i in range(0,n-1):
        desequilibres.append([i, barres[i+1] - barres[i]])  # liste de tuples
    # Trie de la liste en ordre croissant de déséquilibres
    desequilibres = sorted(desequilibres, key=lambda element: element[1])
    max_deseq = k * desequilibres[n-2][1]

    # Calculer le déquilibre de chaque échaffaudage
    # Iteration 1
    paires_list, dep = build_pairs_list(0, n, k, desequilibres)
    result_min = 0
    for i in range(k):                              # Pas assez de paires - ne fonctionne pas
        result_min += paires_list[i][1]

    # Iteration suivantes
    while dep > 0:      # alors il y a d'autres possibilités d'échaffaudages à tester
        paires_list, dep = build_pairs_list(dep, n, k, desequilibres)
        if len(paires_list) == k:
            result = 0
            for i in range(k):
                result += paires_list[i][1]
            if result < result_min:
                result_min = result

    print(result_min)

def build_pairs_list(start: int, n:int, k:int, deseq: List):
    paires = []
    paires.append(deseq[start])
    used_bars = []
    used_bars.append(paires[0][0])
    used_bars.append(paires[0][0]+1)
    start += 1
    ko_index = 0

    i = 1
    while i < k:
        if start < (n-1):       # deseq comprend (n-1) values
            if (deseq[start][0] not in used_bars) and (deseq[start][0]+1 not in used_bars):
                paires.append(deseq[start])     # ajout de la paire à la liste de paires considérées
                used_bars.append(deseq[start][0])
                used_bars.append(deseq[start][0]+1)
                i += 1
            else:
                if ko_index == 0:
                    ko_index = start
            start += 1
        else:
            break    
    return paires, ko_index

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    barres = list(map(int, input().split()))

    # Tests
#    n = 7
#    k = 2
#    barres = [1, 4, 5, 5, 6, 9, 12]
#    n = 5
#    k = 2
#    barres = [10, 6, 4, 1, 3]

    desequilibre_minimal(n, k, barres)