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
    words = [A + B for A in a for B in b]                       # à chaque A on associe un B => forme la phrase voulue
    word_count = Counter(words)                                 #Count les occurrences de chaque mot 
    occurrences = sorted(word_count.values())                   #Extrait la liste des occurrences puis on prend la médiane
    #occurrences = [1,1,15,1]
    print("Occurences : ", occurrences)
    target = sum(occurrences)//len(occurrences)
    corrections = sum(abs(x - target) for x in occurrences)
    print(corrections)
    #if len(occurrences) % 2 == 1:                               # Si len impaire
    #    median = occurrences[len(occurrences) // 2]
    #    #print("median",median)
    #    corrections = sum(abs(x - median) for x in occurrences)
    #else:                                                       # Si len paire
    #    low_median = occurrences[(len(occurrences) // 2)-1]
    #    high_median = occurrences[(len(occurrences) // 2)]
    #    mean  = (low_median+high_median)/2
    #    if type(mean)==int:
    #        corrections = sum(abs(x - mean) for x in occurrences)
    #    else:        
    #        steps_low = sum(abs(x - low_median) for x in occurrences)
    #        steps_high = sum(abs(x - high_median) for x in occurrences)
    #        corrections = min(steps_low, steps_high)                    # Prendre le minimum des deux
#
    #print(corrections)


if __name__ == "__main__":
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    corrections_minimales(n, a, b)

##### RESTE à gérer le cas où la moyenne pour obtenir la médiane n'est pas entière
  #occurrences = [1,2,3,5]
    #if len(occurrences)%2 == 0:
    #    median = (occurrences[(len(occurrences) // 2)-1] + occurrences[(len(occurrences) // 2)])//2
    #    print(median) 
    #else:
    #    median = occurrences[len(occurrences) // 2]                     #Minimise les corrcts avec la médiane
    #print(median)
    #corrections = sum(abs(count - median) for count in occurrences)     #nombre min de corrects


######## Problème si par exemple on a occurences = [1,15,1] ici on affiche 28 alors qu'on devrait afficher 14


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