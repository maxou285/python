# Inverser un chaine (Reverse)
#
# "Bonjour toto"
# "otot ruojnoB"
#
# Boucle
# Slice
#

# Methode Boucle
def reverse_string1(str):
    resultat = ""
    for c in str:
        resultat = c + resultat
        # B
        # oB
        # noB
    return resultat

s = "Bonjour toto"

print(reverse_string1(s))

# Methode Slice (Attention le slice ne marche qu'en python)

print(s[::-1])                          # Rappel print(s[2:6]) print des caractères 3 à 6 de la chaine(njou)
                                        #        print(s[:]) print toute la chaine
                                        #        le 3e paramètre :-1 est le step si le step est de 2 on va écrire un caractère sur 2
                                        #        ici step de -1 signifie qu'on va écrire toute la chaine mais en partant de la fin