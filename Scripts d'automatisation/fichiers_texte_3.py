#FICHIERS TEXTE EXERICE
# "Ecrire des nombres"

# nombres.txt
# 1
# 2
# 3
# 4
# for
# 10 lignes

import os.path
filename = "mon_fichier.txt"
# 1ere Methode

if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()

else:
    print("Le fichier n'existe pas")


# 2e Methode

try:
    f = open(filename, "r")
except FileNotFoundError:
    print("ERREUR : Le fichiern'a pas pu etre ouvert car il n'a pas été trouvé")
else:
    texte = f.read()
    print(texte)
    f.close()

