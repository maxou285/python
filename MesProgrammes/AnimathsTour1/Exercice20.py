compteur = 1
for n in range(1,10000):
    if n**(1/2) == int(n**(1/2)) or n**(1/3)==int(n**(1/3)):
        print("Compteur :" + str(compteur))
        print(n)
        compteur+=1
            