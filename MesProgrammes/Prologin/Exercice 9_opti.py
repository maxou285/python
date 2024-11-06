N = int(input())  # Nombre de tours
sortie = list(map(int, input().split()))  # Profondeur des portes de sortie
entree = list(map(int, input().split()))  # Profondeur des portes d'entrée

# On définit la matrice de coût où cost[i][j] est le coût pour relier la sortie de i à l'entrée de j
cost = [[(sortie[i] - entree[j]) ** 2 for j in range(N)] for i in range(N)]

# Memoisation pour éviter de recalculer les sous-problèmes
memo = [[-1] * (1 << N) for _ in range(N)]
path_memo = [[-1] * (1 << N) for _ in range(N)]  # Pour mémoriser le chemin

def tsp(pos, mask):
    # Si toutes les tours sont visitées, revenir à la première tour
    if mask == (1 << N) - 1:
        return cost[pos][0], [pos]  # Retour au début du cycle

    # Si le résultat est déjà mémorisé
    if memo[pos][mask] != -1:
        return memo[pos][mask], path_memo[pos][mask]

    min_cost = float('inf')
    min_path = []
    
    # Essayer de visiter chaque tour qui n'est pas encore visitée
    for nxt in range(N):
        if (mask & (1 << nxt)) == 0:  # Si la tour `nxt` n'est pas visitée
            new_cost, new_path = tsp(nxt, mask | (1 << nxt))
            new_cost += cost[pos][nxt]
            if new_cost < min_cost:
                min_cost = new_cost
                min_path = [pos] + new_path

    memo[pos][mask] = min_cost
    path_memo[pos][mask] = min_path
    return min_cost, min_path

# Calcul du coût minimal du cycle et chemin associé
min_total_cost = float('inf')
best_path = []

# Essayer de commencer le cycle avec chaque tour
for start in range(N):
    total_cost, path = tsp(start, 1 << start)
    if total_cost < min_total_cost:
        min_total_cost = total_cost
        best_path = path

# Formatage de la sortie
# Ajout de la tour initiale à la fin pour boucler le cycle
best_path = [i + 1 for i in best_path] + [best_path[0] + 1]

print(min_total_cost)
print(" ".join(map(str, best_path)))
