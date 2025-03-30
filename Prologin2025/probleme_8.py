# Concours Prologin 2025
# Probleme : Le juste échaffaudage
# Auteur : Maxou285

# La liste 'desequilibres' comprend la liste des déséquilibres de barres préalablement triés. Comme c'est fait en [i+1]-[i] ça signifie 
# que 2 déséquilibres successifs utilisent une barre en commun. C'est implicite. On connait l'indice des barres par l'index dans le tableau 'desequilibre": 
# ex: desequilibres[5] = desequilibre entre barre_5 et barre_6 = longueur_barre_6 - longueur_barre_5
# Ce qui est cool, c'est que 2 desequilibres non successifs ne peuvent pas utiliser les mêmes barres du coup.   
# < 29/12/2024 :
# . Ok au niveau algo mais ne passe que 6 tests de perf sur 16
# 31/12/2024 :
# . Optimisations : même logique qu'auparavant mais :
#   1. Passage par 3 tableaux au lieu de 2. En utilisant une rotation par pointeur, ça me fait économiser la motié des écritures dans le tableau.
#      Une écriture coute super cher. Par contre, j'utilise plus de mémoire. Effet de bord, je peux parcourir le tableau en ordre croissant.
#   2. Simplification des tests inutiles.
# . Ca me parait toujours super lent. Si ça ne passe pas les tests alors refaire un autre algo dans lequel on trierait aussi les les desequilibres
#   dans l'ordre croissant (en retenant les barres utilisées) et parcourir le tableau un peu comme là en mettant à jour une liste de barres
#   utilisées. Ca permettrait d'implémenter une condition de sortie de boucle plus tôt et d'être super efficace.

from typing import List
#import time
#import tracemalloc  # Pour le suivi de la mémoire
#import random

def desequilibre_minimal(n: int, k: int, barres: List[int]) -> None:
    # Je trie les barres dans l'ordre croissant des longueurs puis je calcule les différences de longueurs d'une barre à l'autre
    barres.sort()
    desequilibres = [barres[i+1] - barres[i] for i in range(n-1)]

    # Initialisation des tableaux desequilibres :
    # deseq_i[x] = contient la somme minimum de x desequilibres non consecutifs en connaissant le desequilibre i (x=nb étage construit)
    # deseq_i_moins_1[x] = même chose mais en connaissant 1 desequilibre de moins (il y a 1 boucle extérieure précédente)
    # deseq_i_moins_2[x] = même chose mais en connaissant 2 desequilibres de moins (il y a 2 boucles extérieure précédentes)
    deseq_i   = [10**18] * (k+1)  # dp[i][*]
    deseq_i_moins_1 = [10**18] * (k+1)  # dp[i-1][*]
    deseq_i_moins_2 = [10**18] * (k+1)  # dp[i-2][*]
    # 0 étage à construire => desequilibre = 0
    deseq_i[0] = 0
    deseq_i_moins_1[0] = 0
    deseq_i_moins_2[0] = 0
    # On démarre avec 1 étage. Du coup, le desequilibre est forcément desequilibres[0]. 
    # Obligé de traiter ce cas à part car on compare avec la version i-1 qui serait négative sinon (cf boucle qui suit)
    deseq_i_moins_1[1] = desequilibres[0]

    # Mise à jour du tableau deseq_i
    # Prise en compte de tous les desequilibres 1 à 1
    for i in range(1, n-1):
        diff = desequilibres[i]                     # permet d'éviter des recherches multiples via index dans la boucle intégroeur
        # Construction de k étages
        for x in range(1, k+1):
            deseq_i[x] = (deseq_i_moins_2[x-1] + diff) if (deseq_i_moins_2[x-1] + diff < deseq_i_moins_1[x]) else deseq_i_moins_1[x]
        # Rotation par pointeur des tableaux
        deseq_i_moins_2, deseq_i_moins_1, deseq_i = deseq_i_moins_1, deseq_i, deseq_i_moins_2

    # Au final, la réponse est dans deseq_i_moins_1[k] (car après le dernier swap, deseq_i_moins_1 correspond à dp[nb_desequilibres-1])
    print(deseq_i_moins_1[k])


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    barres = list(map(int, input().split()))

#    # Tests - result=2
#    n = 7
#    k = 2
#    barres = [1, 4, 5, 5, 6, 9, 12]
#    # Tests - result=4
#    n = 5
#    k = 2
#    barres = [10, 6, 4, 1, 3]
#    # Tests - result=3
#    n = 10
#    k = 4
#    barres = [15, 15, 2, 15, 14, 6, 9, 2, 11, 19]
#    # Tests - k=2 -> 0 ;k=3 -> 0 ;k=4 -> 0 ;k=5 -> 1  ;k=6 -> 2 ;k=7 -> 3 ;k=8 -> 5
#    n = 20
#    k = 8
#    barres = [14, 12, 19, 10, 20, 7, 12, 1, 15, 12, 4, 18, 9, 3, 16, 16, 15, 10, 13, 5]

#    n = 200000
#    k = 250
#    barres = []
#    for i in range(n):
#        barres.append(random.randint(1,1000000000))

#    start_time = time.time()
    #tracemalloc.start()
    #print("\n4:")
    desequilibre_minimal(n, k, barres)
    #print("--- %s seconds ---" % (time.time() - start_time))

    #current, peak = tracemalloc.get_traced_memory()
    #print(f"Current memory usage: {current / 10**6:.2f} MB")
    #print(f"Peak memory usage: {peak / 10**6:.2f} MB")
    #tracemalloc.stop()