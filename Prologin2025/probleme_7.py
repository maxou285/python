# Concours Prologin 2025
# Probleme : Le juste pont
# Auteur : Maxou285

# < 24/12/2024
# Passe tous les tests algo
# Passe aucun tests de perf
# 26/12/2024
# Algo 3 : 2 fois plus rapide d'après les mesures 
# Mais toujours bloqué sur le test 'bait'
# 28/12/2024 
# Ajout d'une condition permettant de ne pas faire de recherche de la meilleure endurance
# si le résultat est forcément moins bon que la meilleure force déjà trouvée. 
# Les tests ont permis de voir qu'on gagnait un temps considérable. Genre on est 10 fois plus rapide qu'avant. 
# SI CA NE PASSE PAS : 
# 1. Tenter une optimisation sur la longueur des zones sures pour la boucle repos. En gros, ne pas tester les longueurs de zone sures
# qui n'existent pas. Pas certain que ça marche mais, objectivement, il y a de fortes chances que R correspondent à une longueur de zone sure 
# existante. 
# 2. Voir comment je peux profiter du fait que les types de sections alternent forcément dans le tableau section. Du coup, on peut savoir à l'avance
# si on traite une zone sure ou une zone fragile. Ca supprime un test dans la fontion peut_traverser.
# 3. Voir en parallélisant les recherches de meilleure_endruance via des threads distincts
# Résultat : test 'bait' ne passe pas
# 29/12/2024
# Opt 1 ci-dessus : utilisation d'un ensemble pour ne tester que les longueurs_sures existantes
# Si ça ne passe toujours pas alors ajouter un tri en ordre décroissant de l'ensemble pour tester les plus grandes valeurs de repos en premier.
# Résultat : ça passe ;-)

from typing import List
#import time
#import tracemalloc  # Pour le suivi de la mémoire
#import random

# Utilisation d'un ensemble qui stocke les longueurs de zones sûres pour ne tester que celles-ci 
def force_maximale(n: int, pont: List[int]) -> None:
    #global cpt_total,cpt_evite
    # Initialisations des variables
    sections = []                                           # transforme le tableau pont en tableau qui contient pour chaque section son type (sur, fragile) et la longueur associée
    type_zone = pont[0]                                     # type_zone est mis en jour en fonction de la progression - permet de déterminer quand on change de type de zone (sure à fragile et fragile à sure)
    longueur_zone = 1                                       # longueur_zone stocke la longueur d'une zone nage/marche - 1 car j'ai déjà traité le premier metre du pont juste avant

    #longueurs_max = [0, 0]                                 # longueurs_max[0] = longueur max d'une zone sure à la sortie de la boucle suivante
                                                            # longueurs_max[1] = longueur max d'une zone fragile à la sortie de la boucle suivante
    longueurs_sures = set()                                 # Ensemble des longueurs uniques des zones sures. Pour optimiser l'ancienne boucle for (1,sure_longueur_max)
                                                            # Je ne testerai que des longueurs existantes
    fragile_longueur_max = 0                                # longueur max d'une zone fragile à la sortie de la boucle suivante

    # Cette boucle en O(n) va faire plusieurs choses à la fois : 
    # 1. Créer le tableau sections qui donne pour chaque section: son type (sure, fragile) et  sa longueur
    # 2. Calcule de la longueur maximale des sections fragiles --> car on a une contrainte sur E puisque E >= longueur max d'une section fragile 
    #                                                              Du coup je gagnerai du temps sur l'évaluation de la meilleure endurance dans l'lgo par dichotomie 
    # 3. Calcule de la maximale des section sures --> car on ne peut pas marcher plus longtemps que la longueur maximale d'une section sure sinon on marcherait sur une section fragile
    #                                                 L'intérêt est de limiter le nombre de valeur de R (repos) possibles. 
    for x in pont[1:]:                                      # Parcours du pont à partir du 2ème mêtre vu qu'on a initialisé le premier mêtre déjà
        if x == type_zone:                                  # On est dans la même section
            longueur_zone += 1                              #   donc on progresse d'un metre
        else:                                               # sinon on change de type de zone 
            sections.append((type_zone, longueur_zone))     #   donc on stocke la section qu'on vient de découvrir avec son type et sa longueur
            if type_zone == 0:                              #   si c'était une zone sure
                longueurs_sures.add(longueur_zone)          #       alors j'ajoute la longueur à l'ensemble de longueur (nouvelle valeur si elle n'existe pas deja)
            else:                                           #       sinon c'est une zone fragile
                fragile_longueur_max = max(fragile_longueur_max, longueur_zone) #   je stocke la plus grande longueur
            type_zone = x                                   # Actualise nouveau type de zone
            longueur_zone = 1                               # Actualise nouvelle longueur à 1 vu qu'on vient de traiter le premier metre
    # Ne pas oublier de traiter la dernière zone
    sections.append((type_zone, longueur_zone))
    if type_zone == 0:
        longueurs_sures.add(longueur_zone)                  
    else:
        fragile_longueur_max = max(fragile_longueur_max, longueur_zone)
    #print("nb sections:", len(sections), " ", sections)
    #print("nb longueurs zones sures:", len(longueurs_sures))
    #print("fragile_longueur_max=",fragile_longueur_max)

    # La fonction peut_traverser vérifie si :
    # . on peut traverser le pont jusqu'au bout en ayant marché au moins une fois pour une valeur de R=repos et un valeur E=endurance fournis en paramètres
    def peut_traverser2(repos, endurance) -> bool:
        nage_courante = 0                                   # Joseph ne nage pas au début du pont. Cette variable contient le nombre de mêtre de nage de Joseph depuis dernièr repos
        marche_au_moins_une_fois = False                    # Au début, Joseph n'a pas marché au moins une fois (contrainte du problème). 
                                                            # Variable pour capturer que j'ai bien marché au moins une fois pendant le parcous
        for t, longueur in sections:                        # Je parcours le pont section par section
            if t == 0 and longueur >= repos:                # Section sure et longueur de la zone supérieure à longueur de repos :
                                                            #   Evaluation short-circuit => 2ème test effectué que si le premier est vrai donc une fois sur deux
                                                            #   car les valeurs de types alternes forcément dans le tableau section
                marche_au_moins_une_fois = True             #   Si c'est le cas alors je capture le fait que j'ai marché au moins une fois (une condition de remplie)
                nage_courante = 0                           #                         je réinitialise la distance de nage car je marche
            else:                                           #   Sinon soit la section est fragile, soit longueur <= repos
                nage_courante += longueur                   #       Je mets à jour la longueur de nage_courante vu que je ne peux pas marcher quand je suis ici
                if nage_courante > endurance:               #       Dans les 2 cas, si nage_courante (que j'ai mise à jour au début)> endurance
                    return False                            #                                  alors je n'ai pas pu traverser le pont
        return marche_au_moins_une_fois                     # J'ai réussi à traverser le pont mais possiblement sans avoir marché au moins une fois

    # Boucle principale : je teste pour toutes les valeurs possibles de repos cad celles qui sont dans l'ensemble longueurs_sures
    meilleure_force = -10**9                                # initialisation à une valeur impossible qui sera forcément modifiée 
    for repos in longueurs_sures:
        # Recherche dichotomique de la meilleure endurance pour la valeur de 'repos'
        bas, haut = fragile_longueur_max, n-1               # Définitions des limites basse et haute pour l'endurance (pour l'algo par dichotomie successives)
                                                            #   endurance min = longueur de la plus longue section fragile au minimum
                                                            #   endurance max = longueur du pont au maximum -1 car on doit marcher au moins une fois
        meilleure_endurance = n-1                           # Comme F=R-E, une valeur de n-1 correspond à la pire valeur endurance.
                                                            # L'objet de la recherche par dichotomie est de la modifier pour une valeur plus faible
        while bas <= haut:                                  # condition de sortie de la recherche dichotomique -> quand la limite basse > limite haute
            milieu = (bas + haut) // 2                      # Découpage de l'échantillonage en 2 parties égales (puis encore par 2, et encore par 2 jusqu'à ce que la zone ne puisse plus être découpée)
            #cpt_total += 1                                  # Capture le nombre de tests effectués au total
            if repos - milieu > meilleure_force:            # Optimisation hyper importante : ce test permet de ne déterminer la meilleure endurance que 
                                                            # si la valeur obtenue à des chances d'être meilleure que la meilleure_force précente. 
                                                            # Facile à calculer car si peut_traverser=True alors force=repos-milieu (milieu=endurance testée) 
                if peut_traverser2(repos, milieu):          #   s'il est possible d'avoirune meilleur force F alors on teste si Joseph peut traverser avec ce repos et cette endurance 
                    meilleure_endurance = milieu            #       si oui alors on capture meilleure_endurance pour cette valeur de repos
                    haut = milieu - 1                       #                 et on redéfinit la moitié dans laquelle recherché la meilleure endurance
                else:                                       #       sinon je n'ai pas pu traverser avec l'endurance (=milieu) donnée pour le repos définit
                    bas = milieu + 1                        #                 Donc je cherche dans l'autre moitié
            else:                                           # Je n'ai pas à trouver une meilleure endurance car je sais que la force F sera inférieur ou égale à la meilleure force que j'ai
                haut = milieu - 1                           #   donc je me place dans la partie à recherchée comme si j'avais réussi
                #cpt_evite += 1                              #   Variable qui me permet d'évaluer le nombre de recherche de meilleure_endurance évités
        meilleure_force = max(meilleure_force, repos - meilleure_endurance)     # Mise à jour de la meilleure_force

    print(meilleure_force)                                  # Imprimer le résultat

if __name__ == "__main__":
    # Commencer le suivi de la mémoire
    #tracemalloc.start()

    n = int(input().strip())
    pont = list(map(int, input().split()))

    # Variables pour comptabiliser le nombre de fois où j'ai évité la mesure d'endurance par dichotomie
    #cpt_evite = 0
    #cpt_total = 0

    # Test 1 - résultat=0
    #n=9
    #pont=[1, 0, 1, 0, 0, 0, 1, 1, 1]
    # Test 2 - résultat=1
    #n=10
    #pont=[1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    #print("pont:",pont)
    # Test - gros N au hazard
    #n = 500000
    #pont = [random.randint(0, 1) for _ in range(n)]
    # Test --- pont=[0,1,0,1, ...]
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(0)
    #    pont.append(1)
    # Test --- pont=[1,0,1,0,1, ...]
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(1)
    #    pont.append(0)
    # Test --- pont=[0,1,1,1,1, ...]
    #pont = []
    #n = 500000
    #pont.append(0)
    #for i in range(n-1):
    #    pont.append(1)
    # Test --- pont=[1,0,0,0,0, ...] - algo 7 ultra rapide sur case alors qu'il est lent sur les autres
    #pont = []
    #n = 500000
    #pont.append(1)
    #for i in range(n-1):
    #    pont.append(0)
    # Test --- pont=[0,0,0,0,1,1,1,1] - algo 7 plante totalement
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(0)
    #for i in range(n//2):
    #    pont.append(1)
    # Test --- pont=[1,1,1,1,0,0,0,0]
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(1)
    #for i in range(n//2):
    #    pont.append(0)
    # Test - [01001000100001 ...]
    # . quand le nombre de longueurs différentes de sections sures est au max (impact la boucle for repos in longueurs_sures)
    # . longueurs_fragile_max = 1 car alors la recherche dichotomique a le plus grand écart possible [1 .. n-1]
    #n = 500000
    #pont = []
    #for i in range(n):          # initalise tableau avec que des 0
    #    pont.append(0)
    #step = 2
    #i = 1                    # le premier 1 est mis en position 1
    #while i < n:
    #    pont[i] = 1
    #    step += 1
    #    i += step
    ##for i in range(n-len(pont)):
    #    pont.append(0)
    # Test --- pont=[00001010] 
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(0)
    #for i in range(n//4):
    #    pont.append(1)
    #    pont.append(0)
    #for i in range(n-len(pont)):
    #    pont.append(0)
    # Test --- pont=[010010001 ... 101010101010]
    #pont = []
    #n = 500000
    #for i in range(n//2):
    #    pont.append(0)
    #step = 2
    #i = 1                    # le premier 1 est mis en position 1
    #while i < n//2:
    #    pont[i] = 1
    #    step += 1
    #    i += step
    #for i in range(n//4):
    #    pont.append(1)
    #    pont.append(0)
    #for i in range(n-len(pont)):
    #    pont.append(0)
    #print(len(pont))
    #print(pont)

    #cpt_evite = 0
    #cpt_total = 0
    #time1=time.time()
    force_maximale(n, pont)
    #print("Time ref: ", time.time()-time1)
    #print("cpt_total=", cpt_total, " cpt_evites=", cpt_evite, "\n")

    # Afficher l'utilisation de la mémoire
    #current, peak = tracemalloc.get_traced_memory()
    #print(f"Current memory usage: {current / 10**3:.2f} KB")
    #print(f"Peak memory usage: {peak / 10**3:.2f} KB")
    #tracemalloc.stop()