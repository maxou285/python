## Code super dégeu, surtout sur la fin mais bon ca permet de passer tous les test
from typing import List


def minimum_exclus(n: int, m: int, criteres: List[List[int]]) -> None:
    """
    :param n: le nombre de sous-marins
    :param m: le nombre de critères
    :param criteres: les critères de chaque sous-marin
    """
    global try_1
    # TODO Afficher le nombre minimum de sous-marins qui ne pourront pas
    # rentrer dans la ville
    nbr_apparence_dans_la_liste = 0
    nb_sous_marin_passé = 0
    for élément in criteres:                                    # On parcout la liste des sous-marins
        criteres.remove(élément)                                # On retire le sous-marin étudié de la liste
        if élément in criteres:                                 # Si les critères de ce sous-marins sont encore présent dans la liste c'est qu'il y en avait 2
                    criteres.remove(élément)                    # On remove le deuxième sous-marin de la paire
        else:
            criteres.append(élément)
    
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    criteres = [list(map(int, input().split())) for _ in range(n)]
    minimum_exclus(n, m, criteres)
    try_1=len(criteres)
    minimum_exclus(n, m, criteres)                              # On relance la fonction avec la nouvelle liste
    if len(criteres)==try_1:
        print(len(criteres))        
    else:
        minimum_exclus(n, m, criteres)
        if len(criteres)==try_1:
            print(len(criteres))        
        else:
            minimum_exclus(n, m, criteres)
            if len(criteres)==try_1:
                print(len(criteres))        
            else:
                minimum_exclus(n, m, criteres)
                if len(criteres)==try_1:
                    print(len(criteres))        
                else:
                    minimum_exclus(n, m, criteres)
                    print(len(criteres))