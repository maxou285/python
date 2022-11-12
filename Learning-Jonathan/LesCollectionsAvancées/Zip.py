

pizzas_nom = ["4 fromages", "Calzone", "Hawai"]
pizzas_prix = [14, 8, 12]

nom_et_prix = list(zip(pizzas_nom, pizzas_prix))

for (nom, prix) in nom_et_prix:
    print(nom + " - " + str(prix) + "€")

unzipped = list(zip(*nom_et_prix))
pn, pp = list(zip(*nom_et_prix))


print("toto")