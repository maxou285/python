# EXTRAIRE LE TEXTE DES FICHIERS PDF
from PyPDF2 import PdfFileWriter,PdfFileReader

f = open("recap.pdf", "rb")

f_reader = PdfFileReader(f)
page0 = f_reader.getPage(0)
texte = page0.extract_text()


# ATTENTION Ici ca dépend des parametres et des différents encodages du fichiers pdf mais certains caractères peuvent potentiellement etre "bizarres"
# Pour régler cet éventuel problème on peut remplacer ces caractères spécifiques par d'autres 
texte = texte.replace("Ò", '"').replace("‘", "è").replace("‹", "à").replace("”", "é").replace("Õ", "'").replace("’", "ê")
# On remplace un caractère (premier paramètre) par un autre (second parametre)
print(texte)

f.close()