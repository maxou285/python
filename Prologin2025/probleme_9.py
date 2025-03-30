# Concours Prologin 2025
# Probleme : La juste muraille
# Auteur : Maxou285

# 01/01/2025 : 
# . Algorithme optimisé à mort selon moi mais à mon avis n'ira pas très loin dans les tests de perf.
# . PAr contre, tous les tests montrent un résultat bitonique --> croissance puis décroissance. C'est surement lié 
#   au fait que les tours sont triées dans les tableaux entree et sortie. 
#   Du coup, il doit y avoir une approche possible pour exploiter ce truc bitonique. 
# . Recherches effectuées qui parlent d'algorithmes branch-and-bound et branch-and-cut.
# . TODO : Faut regarer ça pour aller plus loin
# 04/01/2025 :
# . Planté au 2ème test de perf à cause de la ram
# . Cette version est exactement la même si ce n'est que je n'utilise qu'un seul tableau en n*2^n au lieu de 2
# . Pas sûr que ça passe

from typing import List
#import random
#import time

def meilleure_muraille(n: int, sortie: List[int], entree: List[int]) -> None:
    """
    :param n: le nombre de tours
    :param sortie: la profondeur de la porte de sortie de chaque tour
    :param entree: la profondeur de la porte d'entrée de chaque tour
    """
    # TODO Afficher, sur une première ligne, le coût minimal d'un cycle passant
    # par toutes les tours. Puis, sur une seconde ligne, afficher dans l'ordre
    # les tours visitées par ce cycle, séparées par un espace. Si plusieurs
    # cycles de même coût existent, afficher n'importe lequel d'entre eux.

    valeur_infinie = float('inf')       # Valeur infinie car dans l'ennoncé, il est dit qu'il faire attention au dépassement d'entier

    # Je procéde comme dans l'énnoncé : 
    # Calcule de la matrice décrivant le coût de placer un rempart de n'importe quelle tour i vers n'importe quelle tour j
    couts_tour_i_a_j = [[valeur_infinie]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cout_i_j = sortie[i] - entree[j]
            couts_tour_i_a_j[i][j] = cout_i_j * cout_i_j
    #for i in range(n):
    #    print(couts_tour_i_a_j[i])

    # Comme on est dans un cycle, on peut partir de n'importe quel point du cycle, le total sera le même si on va dans le même sens.
    # A noter que la matrice n'est pas symmétrique (on le voit bien dans l'exemple), du coup parcourir dans l'autre sens aurait un autre coût.
    # Mais du coup, je décide de toujours partir de la tour 0 et aller à chaque autre tour pour revenir au point 0.
    # 
    # 1 tableau :
    # . couts_parcours = contient les couts de tous les parcours testés
    #
    # J'utilise un masque de n bit pour savoir si j'ai utilisé la tour i ou non.
    # . bit i = 0 --> tour i non utilisée dans le parcours étudié
    # . bit i = 1 --> tour i utilisée dans le cparcours étudié
    # Comme les tours sont uniques, ce masque me sert aussi d'indice dans les tableaux 
    # Création du tableau avec valeurs par défaut.
    couts_parcours = [[valeur_infinie]*n for _ in range(1 << n)]    # par défaut, super grande valeur. C'est par rapport à cette valeur qu'on sait si on a un parcours moins couteux ou non
    # Initialisation des couts pour la tour 0 qui est notre tour de départ
    for k in range(1, n):
        couts_parcours[1 << 0 | 1 << k][k] = couts_tour_i_a_j[0][k]   # Départ = toujours tour 0 --> bit_0=1 OR(bitwise) bit_k=1 (tour k utilisée)
    #for i in range(n):
    #    print(i, couts_parcours[i])

    # Remplir la table des couts_parcours
    for parcours in range(1, 1 << n, 2):    # Seuls les parcours qui contiennet la tour 0 en premier doivent être testés
                                            # Donc bit_0 = 1, donc tester tous les parcours impairs, donc de 2 en 2
        # La derniere tour (sans compter la premiere) n'est pas la tour 0. Je les teste toute une à une
        for derniere_tour in range(1, n):
            # Je checke si la dernière tour est bien dans l'itinéraire que je veux tester maintenant = progression dans le parcours précédent
            if not (parcours & (1 << derniere_tour)):
                continue        # Si ce n'est pas le cas je passe au suivant
            # Sinon, je teste pour les tours candidates suivantes
            for tour_suivante in range(1, n):
                if parcours & (1 << tour_suivante):     # La tour suivante est-elle déjà dans le parcours ?
                    continue                            # si OUI alors je passe à la tour suivante
                # Si NON alors :
                # . J'ajoute la nouvelle tour au parcours (opération rapide de bit)
                # . Je mets à jour le cout du parcours jusque là
                # . ET super important, je mets à jour le cout de ce parcours dans le tableau couts_parcours (qui contient tous  
                #   les couts de parcours minimaux) avec l'ajout de cette tour si c'est inférieur au cout que j'avais en ref
                parcours_maj = parcours | (1 << tour_suivante)  # mise à jour (maj) du parcours en activant (mise à 1) le bit correspondant à l'id de la tour suivante
                cout_parcours_maj = couts_parcours[parcours][derniere_tour] +  couts_tour_i_a_j[derniere_tour][tour_suivante]
                if cout_parcours_maj < couts_parcours[parcours_maj][tour_suivante]:
                    couts_parcours[parcours_maj][tour_suivante] = cout_parcours_maj

    # Le parcours utilise toutes les tours en partant de 0. Maintenant, il faut retourner à la première tour au meilleur cout
    # Je dois déterminer quel est le meilleur des parcours complets
    cycle_cout_minimal = valeur_infinie
    tour = -1                          # avant dernière tour inconnue pour le moment
    cycle_complet = (1 << n) - 1       # cycle_complet = tous les bits sotn à 1 (2**n -1 - plus rapide en décallage de bits)
    # Je parcours tous les cycles complets et je calcule le cout total avec le retour depuis la tour k. 
    # Je retiens le plus faible et j'affiche le résultat
    for avant_derniere_tour in range(1, n):
        cout_actuel = couts_parcours[cycle_complet][avant_derniere_tour] + couts_tour_i_a_j[avant_derniere_tour][0]
        if cout_actuel < cycle_cout_minimal:
            cycle_cout_minimal = cout_actuel
            tour = avant_derniere_tour
    print(int(cycle_cout_minimal))

    # Reconstruction du chemin à l'envers. On part de la dernière tour pour aller à la tour 0.
    # Puis je rajoute la tour 0 à la fin et j'affiche le résultat
    cycle_optimal = [0]  # le cycle se termine par la tour 0
    cycle_complet = (1 << n) - 1
    while tour != 0:
        cycle_optimal.append(tour)
        # Il faut déterminer quelle est la tour précédente
        # Pour cela, je cherche celle qui a le monidre cout
        meilleure_tour_precedente = -1                  # valeur impossible
        meilleur_cout = valeur_infinie
        for tour_precedente in range(n):
            if tour_precedente == tour or not (cycle_complet & (1 << tour_precedente)):
                continue
            # Vérifier que tour_precedente est valide avant de faire le décalage
            if tour_precedente < 0 or tour_precedente >= n:
                continue
            cout_parcours = couts_parcours[cycle_complet ^ (1 << tour)][tour_precedente] + couts_tour_i_a_j[tour_precedente][tour]
            # Est-ce la meilleure_tour précédente ?
            if cout_parcours < meilleur_cout:
                meilleur_cout = cout_parcours                   # Si oui, aloes je mets à jour le meilleur_cout
                meilleure_tour_precedente = tour_precedente     # et je garde l'id de la tour bien au chaud et je teste la suivante
        # Cas où on 'a pas trouvé une meilleure tour. On est à la fin du cycle. 
        if meilleure_tour_precedente == -1:
            break  # On sort
        cycle_complet = cycle_complet ^ (1 << tour)   # Tour traitée donc supprimée du cycle complet (XOR)
        tour = meilleure_tour_precedente
    cycle_optimal.append(0)
    cycle_optimal.reverse()
    print(" ".join(map(str, cycle_optimal)))

if __name__ == "__main__":
    n = int(input())
    sortie = list(map(int, input().split()))
    entree = list(map(int, input().split()))

#    n = 3
#    sortie = [1, 2, 3]
#    entree = [1, 4, 5]

#    n = 4
#    sortie = [1, 2, 3, 4]
#    entree = [1, 4, 5, 6]

#    n = 6
#    sortie = [1, 2, 3, 4, 5, 6]
#    entree = [1, 4, 5, 6, 8, 9]

#    n = 20
#    sortie = []
#    entree = []
#    for i in range(n):
#        sortie.append(random.randint(1,1000000000))
#        entree.append(random.randint(1,1000000000))
#    sortie.sort()
#    entree.sort()

#    start_time = time.time()
#    print("Soumis :")
#    meilleure_muraille_soumis(n, sortie, entree)
#    print("--- %s seconds ---" % (time.time() - start_time))

#    start_time = time.time()
#    print("\n2 :")
#    meilleure_muraille2(n, sortie, entree)
#    print("--- %s seconds ---" % (time.time() - start_time))

#    start_time = time.time()
#    print("\n3 :")
#    meilleure_muraille3(n, sortie, entree)
#    print("--- %s seconds ---" % (time.time() - start_time))

#    start_time = time.time()
#    print("\n4 :")
#    meilleure_muraille4(n, sortie, entree)
#    print("--- %s seconds ---" % (time.time() - start_time))

#    start_time = time.time()
#    print("\n5b :")
    meilleure_muraille(n, sortie, entree)
#    print("--- %s seconds ---" % (time.time() - start_time))