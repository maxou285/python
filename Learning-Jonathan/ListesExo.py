nouveau_nom = "titi"
nom = []

while True:
    nouveau_nom = input("Quel est votre nom ? ")
    if nouveau_nom  == "":
        break
    nom.append(nouveau_nom)

print()
print("Nom des personnes : ")
nom.sort()                          # Ordre alphabétique        A-Z puis a-z
for nouveau_nom in nom:
    print("   " + nouveau_nom)
