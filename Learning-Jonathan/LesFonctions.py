#Les Fonctions



"""nom = "toto"
print("Je m'appelle " + nom) #concaténé la chaine <- Un seul paramètre
print("Je m'appelle", nom) #2 paramètres"""

"""nom = input("Quel est votre nom ? : ")
print("Votre nom est " + nom)"""



"""nom1 = input("Nom de la personne 1")
age1 = input("Age de la personne 1")
print("La personne 1 est " + nom1 + " Son age est de "+ age1 + "ans")
print("Le nom comporte " + str(len(nom1)) + " lettres")

nom2 = input("Nom de la personne 1")
age2 = input("Age de la personne 1")
print("La personne 1 est " + nom2 + " Son age est de "+ age2 + "ans")

nom3 = input("Nom de la personne 1")
age3 = input("Age de la personne 1")
print("La personne 1 est " + nom3 + " Son age est de "+ age3 + "ans")"""


#définition de la fonction
#Dans une fonction quand il nous manque des informations comme ici le nom l'age et le nombre de lettre je les mets en paramètre
def afficher_infos_personne(nom="", age = 0): #<-paramètre infos manquantes
  if nom == "":
    print("Vous n'avez pas donnez de nom l'age vaut " + age)
    return
  if age == 0:
    print("La personne est " + nom)    
  else:
    print("La personne est " + nom +" son age est " + str(age) + " ans")
    print("Le nom comporte", len(nom) , "caractères")
  if est_majeur(age):
    print("Il est majeur")
  else:
    print("Il est mineur")
def est_majeur(age):
  # Vrai ou faux (true false)
  # si l'age >= 18 => True sinon False
  if age >= 18:
    return True
  return False        #Ici le else est implicite
print("Début du programme")

afficher_infos_personne(age="20") #Dans l'ordre des paramètres donnés en définition 

#paramètre optionnel si on lui donne une valeur dans la def


age = 21
print("La personne a " + str(age) + " ans")
if est_majeur(age):
  print("Il est majeur")
else:
  print("Il est mineur")

print("Fin du programme")

#Le return (pas obligatoire)
#-> Sortir d'une fonction
#->renvoyer une valeur(pas obligatoire)