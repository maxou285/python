#Le dictionnaire fait partie des collections

personne = {"nom":"Mélanie","age":25,"taille":1.60}         # Syntaxe du Dictionnaire


print(personne)
print(personne["nom"])                                      # affiche uniquement le contenu de la clé "nom" du dictionnaire personne



personne["nom"] = "Claire"                                  # modifie la valeur de la clé nom du Dictionnaire personne
print(personne)



personne["poste"] = "Developpeur"                           # Rajoute une clé "poste" avec comme contenu : "Developpeur " dans le dictionnaire personne
print(personne)


achat = ("chocolat","beurre","fromage")                     
personne["achat"] = achat                                    # Rajoute une clé "achat" avec comme contenu : le contenu du tuple achat déclaré plus haut
print(personne)                                              # dans le dictionnaire personne


for i in personne:
    print("Clef : ",i," -valeur ", personne[i])               # Imprimer tout le contenu du dictionnaire
   

personnes = [
    ("Mélanie", 25, 1,6),
    ("Paul", 29, 1,8),
    ("Jacque",35,1.75),
    ("Martin", 16, 1,65)

]


def obtenir_informations(nom, liste):               # Boucle jusqu'a la clé voulue
    for i in liste:
        if i[0] == nom:                     
            return i
    return None

infos = obtenir_informations("Jacque", personnes)
print(infos)


personnes_dict = {
    "Mélanie": (25, 1,6),
    "Paul" :  (29, 1,8),
    "Jacque":(35,1.75),
    "Martin": (16, 1,65)    
}

infos = personnes_dict["Jacque"]                # Algorythme beaucoup plus puissant car va instantanément à la clé ne boucle pas jusqu'a
print(infos)

#ou

infos = personnes_dict.get("Julie")
if infos == None:
    print("La clé n'existe pas ")
else:
    print(infos)