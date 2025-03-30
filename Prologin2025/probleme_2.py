# Concours Prologin 2025
# Probleme : Le juste semblable
# Auteur : Maxou285

from typing import List
from collections import defaultdict

def minimum_exclus(n: int, m: int, criteres: List[List[int]]) -> None:
    """
    :param n: le nombre de sous-marins
    :param m: le nombre de critères
    :param criteres: les critères de chaque sous-marin
    """
    # on commence par compter les occurrences de chaque configuration de critères disponible
    compteur = defaultdict(int)       # ici on initialise le compteur, => un dictionnaire (avec valeur par défaut de 0) sous la forme clé : 'le critère' value : 'occurence de ce critère'

    for critere in criteres:          # pour chaque critère
        clé = tuple(critere)          # on associe la clé le critere
        compteur[clé] += 1            # et on ajoute l'occurence comme value pour la clé en question
    #print(compteur)

    # La deuxième étape est de calculer le nombre de sous-marins sans paire
    sum = 0
    for sconf in compteur.values():           # on parcourt toutes les configurations de critères prises par les sousm arins
        sum+= sconf %2                        # on regarde modulo 2 si c'est 0 c'est qu'il y a un nombre pair de sous-marins partageant ces critères sinon c'est impaire donc un sous-marins est seul
    
    # plus qu'a afficher le résultat :)
    print(sum)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    criteres = [list(map(int, input().split())) for _ in range(n)]
    minimum_exclus(n, m, criteres)