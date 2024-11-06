from typing import List

def force_maximale(n: int, pont: List[int]) -> None:
    """
    :param n: la longueur (en mètres) du pont
    :param pont: le tableau représentant les zones sûres et les zones fragiles du pont.
    """
    
    def peut_traverser(E, R):
        """
        Vérifie si Joseph peut traverser le pont avec une endurance E et un repos R.
        """
        en_nage = False  # Indicateur pour savoir si Joseph est en train de nager
        repos_compteur = 0  # Compteur pour les mètres de marche après une phase de nage
        i = 0
        a_marche = False  # Vérifie que Joseph a marché au moins une fois

        while i < n:
            if pont[i] == 1:
                # Zone fragile : Joseph doit nager ici
                nage = min(E, n - i)  # Joseph nage jusqu'à E ou jusqu'à la fin de la zone fragile
                i += nage
                en_nage = True
                repos_compteur = 0  # Réinitialise le compteur de repos
            else:
                # Zone sûre : Joseph peut marcher ou nager
                if en_nage:
                    # On vient de terminer une nage, donc Joseph doit marcher au moins R mètres
                    if repos_compteur < R:
                        return False
                    en_nage = False
                    repos_compteur = 1
                    a_marche = True
                    i += 1
                elif repos_compteur >= R:
                    # Joseph peut nager s'il a marché au moins R mètres après la dernière nage
                    en_nage = True
                    nage = min(E, n - i)
                    i += nage
                else:
                    # Joseph marche dans la zone sûre
                    repos_compteur += 1
                    a_marche = True
                    i += 1

        return a_marche
    
    max_force = -1  # Initialisation de la force maximale de Joseph

    # Parcourir toutes les valeurs possibles de E pour maximiser la force
    for E in range(1, n + 1):
        left, right = E, n
        # Recherche binaire pour trouver la plus petite valeur de R pour chaque E
        while left < right:
            R = (left + right) // 2
            if peut_traverser(E, R):
                right = R
            else:
                left = R + 1
        if peut_traverser(E, left):
            max_force = max(max_force, left - E)
    
    print(max_force)

if __name__ == "__main__":
    n = int(input())
    pont = list(map(int, input().split()))
    force_maximale(n, pont)
