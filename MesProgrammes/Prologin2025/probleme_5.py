# Concours Prologin 2025
# Probleme : Les mots justes
# Auteur : Maxou285

from collections import Counter
#import time
from itertools import accumulate
#import tracemalloc

def corrections_minimales(N,A,B):   
    # Opti 1-> sortir de O(n^2) pour le nombre d'occurences de mot, la seule valeur qui m'intéresse
    # nombre d'occurences de syllabes dans A
    occurences_A = Counter()
    for a in A:
        occurences_A[a] += 1

    # nombre d'occurences de syllabes dans B
    occurences_B = Counter()
    for b in B:
        occurences_B[b] += 1
    #print(occurences_B)

    # nombre d'occurences de mots 
    occurences = []
    for cpt_A in occurences_A.values():
        for cpt_B in occurences_B.values():
            occurences.append(cpt_A*cpt_B)
    #occurences.sort()    
    #occurences = sorted(occurence)
    #occurences = [1,999]
    occurences = sorted(occurences, reverse=True)
    #print(occurences)
    # Ensuite voici comment l'on va procéder pour trouver la solution minimale : 
    # Un fois la liste triée on va vouloir retirer les plus petites valeurs les unes après les autres => on les ajoute à notre cout total
    #  on calcul la médiane et l'écart total à la median et enfin pour chaque médiane on calculera les écarts des élements avec la fonction cost()

    # la ligne qui suit est légèrement technique, on veut calculer les sommes cumulés des occurences donc on va appliquer la fonction accumulate, pour cela on va d'abord renverser notre liste
    # d'occurences qui est décroissante pour le moment, une fois nos sommes cumulées calculées et sauvegardées dans une liste on inverse cette liste pour retrouver nos sommes dans le bon sens
    sums = list(accumulate(occurences[::-1]))[::-1] + [0]          # rappel : [::-1] inverse la liste, on ajoute ensuite 0, pas pris comme somme, si c'est plus efficace
    medians = [occurences[i // 2] for i in range(len(sums))]       # liste des médianes, potentielles target pour les sommes cumulées calculées

    def cost(indice, median):
        mid = indice // 2                                           
        # la suite va calculer pour une certaine médiane (notre target) le cout totale des modifications (ajout ou suppresion d'occurences) =>  manipulation algébrique pour calculer 
        # cela avec les sommes cumulées c'est le point important qui permet de faire fonctionner cet algo
        total = sums[0] - 2*sums[mid] + 2*sums[indice] - median*(2*mid - indice)         # sums[0] : somme totale des occ, sums[mid] : sommes cumulées jusqu'a mid, sums[indice] : sommes cumulées jusqu'a indice
        return abs(total)                                           # et on oublie pas de prendre la valeure absolue

    meilleur_cout = 10**18                                         # cette valeur impossible sera forcément modifiée
    for indice,median in enumerate(medians):                        # on parcours la liste des médianes avec les indices de chaque
        meilleur_cout = min(meilleur_cout,cost(indice,median))    # on actualise dés qu'on trouve un cout moins élevé
    print(meilleur_cout)
    



if __name__ == "__main__":
    N = int(input())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(N)]
    #time1 = time.time()
    #tracemalloc.start()
    corrections_minimales(N,A,B)
    #corrections_minimales([1,999])
    #print(time.time()-time1)
    #current, peak = tracemalloc.get_traced_memory()
    #print(f"Current memory usage: {current / 10**3:.2f} KB")
    #print(f"Peak memory usage: {peak / 10**3:.2f} KB")
    #tracemalloc.stop()
