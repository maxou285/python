# PyPDF2
# COMBINER

# lire des PDF extraire le texte
# Ecrire des PDF
#   - Combiner 
#   - Rotation, superposer
#   - Ne peut pas : rajouter du texte ou des images

from PyPDF2 import PdfFileWriter, PdfFileReader

contenu_sortie = PdfFileWriter()

fichier_pdf_presentation = open("presentation.pdf", "rb")           # en plus du "r" pour read on rajoute un b pour ouvrir le fichier en mode binaire 
fichier_pdf_recap = open("recap.pdf", "rb")                         # car le format de open par défaut est txt et la on ouvre un pdf

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

print("Nombre de pages du fichier récap : " + str(reader_recap.getNumPages()))
print("Nombre de pages du fichier présentation : " + str(reader_presentation.getNumPages()))

contenu_sortie.addPage(reader_presentation.getPage(0))  #.rotateClockwise(90)  # Tourner la page de 90° dans le pdf
for i in range(reader_recap.getNumPages()):
    contenu_sortie.addPage(reader_recap.getPage(i))


fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()