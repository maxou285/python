# Concours Prologin 2025
# Probleme : Le juste chemin
# Auteur : Maxou285

from collections import deque
from dataclasses import dataclass
from typing import List
#import time
#import random

MOD = 1000000007
sum=0

@dataclass
class Route:
    """une route bidirectionnelle reliant deux maisons"""
    a: int  # la première maison
    b: int  # la seconde maison


def score_total(n: int, m: int, k: int, scores: List[int], routes: List[Route]) -> None:
    global sum
    """
    :param n: le nombre de maisons
    :param m: le nombre de routes
    :param k: le temps restant à Joseph, soit la longueur maximale d'un chemin juste
    :param scores: le score associé à chaque maison
    :param routes: la liste des routes
    :return: Affiche, sur une ligne, la somme des scores des paires de maisons justes, modulo 1_000_000_007.
    """

    # On commence par construire notre graphe comme une liste d'adjacence
    graphe = [[] for _ in range(n)]
    for route in routes:
        # (on retire 1 pour 'raccorder' les index python aux numéros des maisons)
        a = route.a - 1
        b = route.b - 1
        
        graphe[a].append(b)                # on ajoute au graphe 
        graphe[b].append(a)            



    # On utilise un algorithme de parcours en largeur très optimisé
    # je me suis largement inspiré du site : https://marcarea.com/weblog/2019/02/17/parcours-de-graphes-en-python
    # on commence par intialiser la distance des maisons à -1 valeur impossible qui de toutes façons sera modifée et la maison d'oxygène à elle même donc 0
    distance, distance[0] = [-1]*n, 0
    queue = deque([0])

    while queue:                            # on rentre dans la file du parcours
        node_1 = queue.popleft()                 #défile la première maison de la file d'attente
        for adjacent_node in graphe[node_1]:                    # on regarde ensuite les voisins 
            if distance[adjacent_node] == -1:           # -1=> la maison n'as pas été visité
                distance[adjacent_node] = distance[node_1] + 1   # mise à jour de la distnace        
                queue.append(adjacent_node)                 # on l'ajoute à la file

    # On regroupe les scores par distance, pour la suite S[d] représente la somme des scores des maisons à distance d de la maison d'oxygène
    # et onn ne considère que les distances <= k
    S = [0]*(k+1)           # on initialise tous à 0
    #print(S)
    for i in range(n):
        d = distance[i]         # on récupère la distance de la maison i à la maison d'oxygène
        if (d!= -1) and (d <= k):  # puis on regarde si elle est atteignable
            S[d]= (S[d] + scores[i])%MOD # si oui on ajoute son score à S[d]
    #print(distance)
    # Calcul des sommes NewS[X] = somme des S[d]
    NewS, NewS[0] = [0]*(k+1), S[0]           # intialisation de notre nouvelle liste à 0 et de NewS[0] = S[0]
    # pour chaqeu distance on a NewS[d] qui est la somme de NewS[d-1] (jusqu'a la dsitance précédente) et S[d] le score des maisons à une distance d
    for distance in range(1, k+1):
        NewS[distance]=(NewS[distance - 1] + S[distance])%MOD          
     # Enfin on calcule la somme finale  
    for distance in range(0,k+1):     
        sum=(sum + S[distance]*NewS[k - distance])%MOD             # [S[d1]*S[d2])]<=S[d2]=NewS[k-d1]

    # On affiche le résultat :)
    print(sum)
    
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    scores = list(map(int, input().split()))
    routes = [Route(*map(int, input().split())) for _ in range(m)]
    #print(routes)
    #n = random.randint(2,30000)
    #m = random.randint(1,30000)
    #k = random.randint(1,n)
    #scores = []
    #for i in range(1,n+1):
    #    scores += [random.randint(1,1000000006)]
    #routes = [Route(*map(int, (random.randint(1,n),random.randint(1,n)))) for _ in range(m)]
    #print(routes)
    #time1 = time.time()
    score_total(n, m, k, scores, routes)
    #print("Time : ", time.time()-time1)
    #time2=time.time()
    #score_total_2(n, m, k, scores, routes)
    #print("Time : ", time.time()-time2)
