for i in range(0, 5):     #syntaxe principal de la boucle for
  print(i)

#On peut utiliser "jusqu'a une valeure de variable dans un paramètre" par exmple:
nom1 = input("Quel est votre nom ? ")
NB_PERSONNES = 3

def afficher_informations_personnes(nom):
  global nom1
  print()
  print("Vous vous appellez " + nom)
  print("L'an prochain vous aurez " )

for i in range(0, NB_PERSONNES):
  print(i)
  nom = "personne" + str(i+1)
  afficher_informations_personnes(nom)