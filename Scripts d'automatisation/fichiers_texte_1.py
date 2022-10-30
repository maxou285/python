# FICHIERS TEXTE
#
# ouvrir (open) <- nom du fichier, mode
# ecrire (write)/ lire (read)
# fermer (close)

f = open("mon_fichier.txt", "w")

#f.write("Bonjour")
#f.write("Bonjour")
l = ["Première phrase ", "Deuxième phrase ", "Troisièmre phrase "]

f.writelines(l)
f.write("\nFin")


f.close()
