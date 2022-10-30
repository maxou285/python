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

if not os.path.exists("toto"):                          # vérifie si le repertoire toto existe déja ou pas
    os.mkdir("toto")                                    # si il n'existe pas encore => le créer 

#if os.path.exists("toto"):                              # vérifie si le repertoire toto existe ou pas
#    os.rmdir("toto")                                    # si il existe le => le supprimer

filename = os.path.join("rep","mon_fichier.txt")        # équivaut à rep/mon_fichier.txt mais c'est mieux car ca marche sur tous les os 
print("filename : " + filename)                         # rep/mon_fichier.txt ne marcherait pas sur windows car sur windows c'est un \ et pas un /
# 1ere Methode

if os.path.exists(filename):                            # vérifie si le fichier existe
    print("Le fichier existe")          
    f = open(filename, "r")                             # si oui l'ouvrir
    texte = f.read()                                    # lire tout le fichier
    print(texte)        
    f.close()                                           # fermer le fichier

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
if os.path.exists(filename):
    os.remove(filename)                         # supprimer un fichier