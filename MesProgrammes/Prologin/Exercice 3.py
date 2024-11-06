


from typing import List


def force_maximale(longueur: int, tunnel: List[int]) -> None:
    
    #:param longueur: la longueur (en mètres) du passage souterrain
    #:param tunnel: le tableau représentant les zones sûres et les zones de danger du passage souterrain. Un chiffre par mètre : Un `0` correspond à une position dans une zone sûre, et un `1` correspond à une position dans une zone de danger

    
    # TODO Afficher la valeur de force maximale que Joseph Nageant peut obtenir
    # en passant le tunnel.
    max_esquive = 0  # Représente la valeur de E (longueur maximale d'une séquence de zones dangereuses)
    min_repos = float('inf')  # Représente la valeur de R (longueur minimale d'une séquence de zones sûres)
    
    # Variables pour parcourir les séquences
    current_length = 0
    in_danger = tunnel[0] == 1  # True si on commence dans une zone dangereuse, False sinon

    for i in range(longueur):
        if tunnel[i] == 1:  # Zone dangereuse
            if not in_danger:  # Transition depuis une zone sûre
                # Mettre à jour min_repos
                if current_length > 0:
                    min_repos = min(min_repos, current_length)
                # Réinitialiser la longueur actuelle pour la zone dangereuse
                current_length = 1
                in_danger = True
            else:
                current_length += 1  # On continue dans la zone dangereuse
        else:  # Zone sûre
            if in_danger:  # Transition depuis une zone dangereuse
                # Mettre à jour max_esquive
                max_esquive = max(max_esquive, current_length)
                # Réinitialiser la longueur actuelle pour la zone sûre
                current_length = 1
                in_danger = False
            else:
                current_length += 1  # On continue dans la zone sûre
    
    # Mettre à jour pour la dernière séquence
    if in_danger:
        max_esquive = max(max_esquive, current_length)
    else:
        min_repos = min(min_repos, current_length)

    # Si aucune zone sûre n'est trouvée, alors il n'y a pas de repos possible
    if min_repos == float('inf'):
        min_repos = 0  # Pas de repos possible si le tunnel est entièrement dangereux
    
    # Calcul de la force
    force_maximale = min_repos - max_esquive
    return force_maximale, min_repos, max_esquive


if __name__ == "__main__":
    longueur = int(input())
    tunnel = list(map(int, input().split()))
    force, R, E = force_maximale(longueur, tunnel)
    print(force)

