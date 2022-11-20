import random

ALPHABET_MIN = [ chr(i) for i in range(97,123) ]
ALPHABET_MAJ = [ chr(i) for i in range(65,91) ]
CHIFFRES = [ chr(i) for i in range(48,58) ]
CARACTERES_SPECIAUX = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

mot_de_passe = ""
nb_caracteres = input("Combien de caractères pour votre mot de passe ? ")

for i in range(0, int(nb_caracteres)):
    randomcara = random.randint(0,3)
    if randomcara == 0:
        mot_de_passe += str(ALPHABET_MAJ[random.randint(0,25)])
    elif randomcara == 1:
        mot_de_passe += str(ALPHABET_MIN[random.randint(0,len(ALPHABET_MIN)-1)])
    elif randomcara == 2:
        mot_de_passe += str(CHIFFRES[random.randint(0,len(CHIFFRES)-1)])
    elif randomcara == 3:
        mot_de_passe += str(CARACTERES_SPECIAUX[random.randint(0,len(CARACTERES_SPECIAUX)-1)])

print(mot_de_passe)