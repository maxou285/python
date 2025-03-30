# Concours Prologin 2025
# Probleme : Le juste etal
# Auteur : Maxou285

from collections import defaultdict
from typing import List

# Constantes 
########################################################################
MOD = 10**9+7  # On définit notre modulo comme constante à 1 000 000 007
########################################################################
def le_juste_etal(n: int, valeur: int, boites: List[int]) -> None:
    """
    :param n: le nombre de boites
    :param valeur: la valeur du marché du jour
    :param boites: le contenu de chaque boite
    """
    # TODO Afficher, sur une ligne, un unique entier : le nombre de séries
    # justes modulo $1,000,000,007$.
   
   # On commence par quelques initialisations  ci dessous : 
    sum = [0]*(n+1)       # toutes les sommes à 0 au début 
    cpt_reste = defaultdict(int)
    cpt_series, cpt_reste[0] = 0, 1
    #cpt_reste  :  initialise le dictionnaire pour compter les occurrences de chaque reste modulo 'valeur'
    #cpt_series :  initialisation du compteur de séries justes
    #print(sum)

    # Boucle principale : on compte les nombre d'occurences de chaque reste et on actualise cpt_series
    for i in range(1, n+1):                                   
        sum[i] = (sum[i-1] + boites[i-1])%valeur          # Mise à jour de la somme d'indice i (la somme i-1)
        reste = sum[i]                                    # Et on récupère le reste de la somme modulo 'valeur'
        cpt_series+= cpt_reste[reste]                     # On ajoute à notre compteur du début le nombre de fois que ce reste est passé
        cpt_reste[reste]+= 1                              # On incrémente le compteur du reste en question

    print(cpt_series%MOD)                      # plus qu'a afficher le nombre de série modulo MOD


if __name__ == "__main__":
    n = int(input())
    valeur = int(input())
    boites = list(map(int, input().split()))
    le_juste_etal(n, valeur, boites)