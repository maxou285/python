# FICHIERS TEXTE
#
# ouvrir (open) <- nom du fichier, mode
# ecrire (write)/ lire (read)
# fermer (close)

f = open("mon_fichier.txt", "r")

#texte = f.read()                #  lire le fichier en entier
#texte = f.read(2)               # lire uniquement les 2 premiers caractères du fichiers
#texte = f.readline()            # lire 1 seule ligne du fichier
#texte = f.readlines()            # retourne une collection/liste contenant toutes les lignes du fichier
#print(texte)
for line in f:
    print(line, end="")
f.close()