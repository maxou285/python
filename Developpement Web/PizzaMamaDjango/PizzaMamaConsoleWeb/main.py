from xml.etree.ElementTree import PI
import requests
import json

url = "https://maximedurand.pythonanywhere.com/api/GetPizzas"


data = requests.get(url)

#print(data.text)

pizzas = json.loads(data.text)
#print(pizzas)
#print(len(pizzas))

print("Liste des pizzas : ")

for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['nom'] + " : " + str(pizza['prix']) + "€")
