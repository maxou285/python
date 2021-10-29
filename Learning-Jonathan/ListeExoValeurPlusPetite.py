# LISTES ALGO VALEUR LA PLUS PETITE


nom_chauffeurs = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]   
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]



#V1
"""index_min = 0                                    # Algorythme  pour trouver la plus petite valeur
distance_min = distance_chauffeur_km[0]
for i in range (len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i


print("Distance minimale : ", distance_min)
print("Index de la distance maximum : ", index_min)
print("Nom du chauffeur : ", nom_chauffeurs[index_min])"""

distance_chauffeur_km.sort()                            # En utilisant la fonction .sort on trouve aussi la plus petite valeur car elle tri du plus petit
print(distance_chauffeur_km[0])                         # au plus grand

#V2

"""noms_et_distances = [("Patrick", 1.5), ("Paul", 2.2), "Marc", 0,4]


nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:             # < not supported between instances of str and float
         nom_et_distance_min = nom_et_distance

print("Distance minimale : ", nom_et_distance_min[1],"nom du chauffeur", nom_et_distance_min[0])"""