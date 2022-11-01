# FAIRE DES APPELS RÉSEAU AVEC REQUESTS
#
# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

import requests
import json

# API REST 


reponse = requests.get("https://codeavecjonathan.com/res/pizzas1.json")                                                       
print(reponse.status_code)                                                      # quand tout se passe bien le status code est 200
print(reponse.encoding)                                                         # quand le page n'est pas trouvé le status code est 404 

if reponse.status_code == 200:
    reponse.encoding = "utf-8"                                                      # modifier l'encodage pour corriger les problèmes d'affichage d'accents etc
    print(reponse.text)
    pizzas = json.loads(reponse.text)
    print("Nombre de pizzas : " + str(len(pizzas)))
    print(pizzas[3])
    pizza = pizzas[int(input("Rentrez un numero de pizza : "))]
    print("Nom : " + pizza["nom"])
    print("Ingrédients : " + ", ".join(pizza["ingredients"]))
    print("Prix : " + str(pizza["prix"]))
else:
    print("ERREUR code : " + str(reponse.status_code))


'''
reponse = requests.get("https://codeavecjonathan.com/res/programmation.txt")                                                       
print(reponse.status_code)                                                      # quand tout se passe bien le status code est 200
print(reponse.encoding)                                                         # quand le page n'est pas trouvé le status code est 404 

if reponse.status_code == 200:
    reponse.encoding = "utf-8"                                                      # modifier l'encodage pour corriger les problèmes d'affichage d'accents etc
    print(reponse.text)
else:
    print("ERREUR code : " + str(reponse.status_code))
    '''