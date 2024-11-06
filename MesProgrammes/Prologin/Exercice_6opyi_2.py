from dataclasses import dataclass
from typing import List
from collections import deque

MOD = 1_000_000_007

@dataclass
class Route:
    """une route bidirectionnelle reliant deux maisons"""

    a: int  # la première maison
    b: int  # la seconde maison


def score_total(n: int, m: int, k: int, scores: List[int], routes: List[Route]) -> None:
    """
    :param n: le nombre de maisons
    :param m: le nombre de routes
    :param k: le temps restant à Joseph, soit la longueur maximale d'un chemin juste
    :param scores: le score associé à chaque maison
    :param routes: la liste des routes
    """
    # Création du graphe
    graph = [[] for _ in range(n + 1)]
    for route in routes:
        graph[route.a].append(route.b)
        graph[route.b].append(route.a)
    
    # Initialisation de la matrice de distances
    distances = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distances[i][i] = 0
    
    # Remplissage de la matrice de distances avec les routes directes
    for route in routes:
        distances[route.a][route.b] = 1
        distances[route.b][route.a] = 1
    
    # Algorithme de Floyd-Warshall pour calculer les distances minimales entre toutes les paires de maisons
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    # Calcul de la somme des scores des paires justes
    total_score = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distances[1][i] + distances[i][j] <= k:
                total_score += scores[i - 1] * scores[j - 1]
                total_score %= MOD
    
    # Afficher le résultat
    print(total_score)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    scores = list(map(int, input().split()))
    routes = [Route(*map(int, input().split())) for _ in range(m)]
    score_total(n, m, k, scores, routes)