from dataclasses import dataclass       # Permet de créer des classes de données simples. Ici, elle est utilisée pour définir la classe Route
from typing import List                 
from collections import deque, defaultdict # Fournissent une file d'attente (FIFO) pour les parcours en largeur (BFS) et un dictionnaire avec valeurs par défaut (ici, une liste).

MOD = 1000000007

@dataclass
class Route:
    """Une route bidirectionnelle reliant deux maisons."""
    a: int  # La première maison
    b: int  # La seconde maison

# Cette fonction implémente l'algorithme de parcours en largeur (BFS) pour calculer  la distance minimale de la maison start (numéro 1) à toutes les autres maisons du graphe.
def algo_distances(graph, start, n): 
    distances = [-1] * n            # Initialise distances, un tableau de tailles des chemins vers chaque maison avec la valeur -1 (non accessible), et met la distance de start à zéro. 
    queue = deque([(start, 0)])
    distances[start] = 0
    
    while queue:                    # Pour chaque maison visitée, met à jour la distance pour ses voisins (non encore visités) à depth + 1 et les ajoute dans la file.
        current, depth = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # Maison non visitée
                distances[neighbor] = depth + 1
                queue.append((neighbor, depth + 1))
    return distances                  #Retourne distances, qui contient les distances minimales de la maison 1 à chaque autre maison.

def score_total(n: int, m: int, k: int, scores: List[int], routes: List[Route]) -> None:
    """
    Affiche la somme des scores des paires de maisons justes, modulo $1\,000\,000\,007$.
    
    :param n: le nombre de maisons
    :param m: le nombre de routes
    :param k: le temps restant à Joseph, soit la longueur maximale d'un chemin juste
    :param scores: le score associé à chaque maison
    :param routes: la liste des routes
    """
    # Construction du graphe des maisons
    # Construire le graphe sous forme de dictionnaire où chaque maison pointe vers ses voisins.
    graph = defaultdict(list)
    for route in routes:
        graph[route.a - 1].append(route.b - 1)
        graph[route.b - 1].append(route.a - 1)
    distances_from_1 = algo_distances(graph, 0, n)      # Calculer les distances de la maison 1 aux autres maisons en appelant algo_distances().
    
    # Identifier les maisons accessibles en ≤ k minutes (distance maximale k).
    reachable_houses = [i for i in range(n) if distances_from_1[i] != -1 and distances_from_1[i] <= k]
    result = 0
    
    # Calcul de la somme des score
    # Pour chaque paire de maisons a et b parmi celles accessibles, vérifie si la paire peut être visitée en moins de k minutes (somme des distances de a et b vers la maison 1).
    for i in range(len(reachable_houses)):
        for j in range(i, len(reachable_houses)):
            a = reachable_houses[i]
            b = reachable_houses[j]
            if distances_from_1[a] + distances_from_1[b] <= k:      
                if a == b:                                               # Si a et b sont la même maison, ajoute scores[a] * scores[b] au résultat.
                    result = (result + scores[a] * scores[b]) % MOD
                else:                                                    #  Sinon, ajoute deux fois le produit des scores (car la paire est comptée dans les deux sens).
                    result = (result + 2 * scores[a] * scores[b]) % MOD  


    print(result)

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    scores = list(map(int, input().split()))
    routes = [Route(*map(int, input().split())) for _ in range(m)]
    score_total(n, m, k, scores, routes)

# Pseudo-code:
# 1. Construire le graphe sous forme de liste d'adjacence en utilisant les routes fournies.
# 2. Calculer les distances minimales de la maison 1 à toutes les autres maisons en utilisant un parcours BFS.
# 3. Identifier toutes les maisons accessibles en moins de k minutes.
# 4. Pour chaque paire de maisons (A, B) parmi les maisons accessibles :
#     a. Vérifier si leur distance combinée vers la maison 1 respecte la limite de k minutes.
#     b. Si oui, calculer leur produit de scores.
#     c. Ajouter ce produit au résultat, en prenant en compte le sens de la paire.
# 5. Afficher la somme des scores des paires justes modulo 1 000 000 007.
