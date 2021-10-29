
def afficher(collection,pizza_affichés=-1):
    collection.sort()
    if collection == vide:
        print("AUCUNE PIZZAS")
        return
    print("----------LISTE DES PIZZAS----------" + " ( " + str(len(collection)) + " ) ")
    if pizza_affichés != -1:
        for i in collection[0:pizza_affichés]:
            print(i)
        print()
        print("Première pizzas : ",collection[0])
        print("Dernière pizzas : ",collection [-1])
        return
    for i in collection:
        print(i)
    print()
    print("Première pizzas : ",collection[0])
    print("Dernière pizzas : ",collection [-1])


def ajouter_pizzas_utilisateur(collection):
    global addpizzas
    addpizzas = input("Pizzas à ajouter : ")
    addpizzas = addpizzas.lower()
    if addpizzas in collection:
        print("ERREUR : Cette pizza existe déja ")
        ajouter_pizzas_utilisateur(pizzas)  
    else:
        pizzas.append(addpizzas)
    

#def pizza_exist(e, collection):
#   for i in collection:
#       if i == e:
#        return True
#   else:
#        return False




pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
vide = ()

ajouter_pizzas_utilisateur(pizzas)
afficher(pizzas,3)
#pizza_exist(addpizzas,pizzas)