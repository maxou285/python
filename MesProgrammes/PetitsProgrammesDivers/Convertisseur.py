# Epreuve de code 1 
# Convertisseur pouce => cms

print("Convertisseur")
mode = input("Choisissez la conversion à réaliser : \n  1) pouces => cms\n  2) cms => pouces\nChoix : ")
valeur = input("Rentrez la valeur à convertir : ")
valeur = float(valeur)
if mode ==  "1":
    valeur_convert = valeur*2.54
    print(str(valeur_convert))
else: 
    valeur_convert = valeur*0.394
    print(str(valeur_convert))
