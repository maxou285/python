from collections import Counter
from typing import List
import random


def corrections_minimales(n: int, a: List[str], b: List[str]) -> None:
    """
    :param n: le nombre de syllabes dans chaque liste
    :param a: les syllabes de début de mot
    :param b: les syllabes de fin de mot
    """
    # TODO Afficher, sur une ligne, le nombre de corrections minimal pour
    # rendre la phrase juste.
    # Génère tous les mots possibles en concaténant chaque syllabe de A avec chaque syllabe de B
    corrections = 0                                     
    steps_low = 0
    steps_high = 0
    words = [A + B for A in a for B in b]                       # à chaque A on associe un B => forme la phrase voulue
    word_count = Counter(words)                                 # Compte les occurrences de chaque mot 
    occurrences = sorted(word_count.values())                   # Extrait la liste des occurrences
    occurrences = sorted([7,1,1,1,1,2])
    if len(occurrences) % 2 == 1:                               # Si len(occurences) impaire
        median = occurrences[len(occurrences) // 2]
        for x in occurrences:
            if abs(x)<abs(x-median):                            # Si il est plus rapide de supprimer les occurences du mot que d'ajouter ou retirer jusqu'a la médiane
                corrections += abs(x)
            else:
                corrections += abs(x-median)
    else:                                                       # Si len(occurences) paire
        low_median = occurrences[(len(occurrences) // 2)-1]     # Médiane inférieure et supérieure
        high_median = occurrences[(len(occurrences) // 2)]
        for x in occurrences:
            if abs(x)<abs(x-low_median):                        # Si il est plus rapide de supprimer les occurences du mot que d'ajouter jusqu'a la médiane
                steps_low += abs(x)
            else:
                steps_low += abs(x-low_median)
        for x in occurrences:
            if abs(x)<abs(x-high_median):                       # Si il est plus rapide de supprimer les occurences du mot que d'ajouter jusqu'a la médiane
                steps_high += abs(x)
            else:
                steps_high += abs(x-high_median)
        corrections = min(steps_low, steps_high)                    # Prendre le minimum des deux
    print(corrections)


if __name__ == "__main__":
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    corrections_minimales(n, a, b)


###### TESTS
    #alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #n = random.randint(1,10)
    #a = []
    #b=[]
    #for i in range(n):
    #    a.append(alphabet[random.randint(0,2)]+alphabet[random.randint(0,2)])
    #for i in range(n):
    #    b.append(alphabet[random.randint(0,2)]+alphabet[random.randint(0,2)])
    #print("ENTREE : \n n : ", n, "\n a : ", a, "\n b : ", b)
    #corrections_minimales(n, a, b)


    #Maximal delete, pour l'entrée    occurrences = [7,1,1,1,1,2] la réponse devrait être 6 mais on trouve 7 par contre avec occurrences = [7,1,1,1,1,1,1] on trouve bien 6