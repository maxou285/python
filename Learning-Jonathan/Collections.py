# Collections : Tableaux, listes, tuples...
# Contenir et gérer plusieurs éléments
# Tuple : immutable pas modifiable
# Liste : mutable modifiable    

"""a = 5
b = "toto"
# TUPLES
personnes = ("Mélanie", "Jean", "Martin", "Alice")
#print(len(personnes))
#print(personnes[-1])           # négatif pour partir de la fin

#for i in range(0,len(personnes)):
#   print(personnes[i])

#for i in personnes:
#    print(i)
#   print(len(i))
#    print(i[0])                 # Affiche la première lettre


#valeurs = range(1,10)
#print(valeurs[-1])

# LISTES

personnes = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"

print(personnes)

personnes.append(nouvelle_personne)                 # personnes.append rajoute le contenu de nouvelle_personne dans la liste personnes
del personnes[1]                                    # del supprime le contenu à l'index 1 dans personnes ici Jean 

print(personnes)


def afficher_personnes(c):
    for i in c:
        print(i)



def modifier_valeurs(a):
    a[0] = 10 


test = [1, 2, 3, 4]
print(test)
modifier_valeurs    (test)
print(test)"""


# FONCTIONS ET TUPLES

"""def obtenir_informations():
    return "Mélanie", 37, 1.60              # En réalité ici on return un tuple seulement dans un return pas besoin des ()

def afficher_informations(nom, age, taille):
    print(f"Informations : Nom : {nom} , Age : {age} , Taille : {taille}")

infos = obtenir_informations()
afficher_informations(*infos)                   # L'étoile devant donne l'ordre d'ouvrir le tuple sinon la fonction pensera que infos est un premier paramètre
print("Nom : " , infos[0])
print("Age : ", infos[1])
print("Taille : " , infos[2])

print(infos)
print(*infos)    # Unpack le tuple           # == print(infos[0],infos[1],infos[2]) 
# nom, age, taille = obtenir_informations()               # On remplit les 3 variables grace au return des 3 valeurs de la fonction
#   afficher_informations(nom, age, taille)"""


# LES SLICES

# Les slices permettent de n'afficher que de l'index 2 a l'index 5 par exemple  ou avec le step d'en sauter 1 sur 2 (::2)

personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")

# [start:stop:step]


for i in personnes[0:5:2]:
    print(i)
