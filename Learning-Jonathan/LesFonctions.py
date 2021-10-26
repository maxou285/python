#Les Fonctions



"""nom = "toto"
print("Je m'appelle " + nom) #concaténé la chaine <- Un seul paramètre
print("Je m'appelle", nom) #2 paramètres"""

"""nom = input("Quel est votre nom ? : ")
print("Votre nom est " + nom)"""


"""
récupérer_etafficher_infos_personnes
  -> récupérer_infos_personnes()
  -> afficher_infos_personnes(nom, age)
    ->est_majeur

"""


def est_majeur(age: int):
  # Vrai ou faux (true false)
  # si l'age >= 18 => True sinon False
  if age >= 18:
    return True
  return False        #Ici le else est implicite

def recuperer_infos_personne(numero_personne):
  nom_personne = input("Nom de la personne " + str(numero_personne))         #local à la fonction contexte local donc peut importe leur nom
  age_personne = input("Age de la personne " + str(numero_personne))
  return nom_personne, int(age_personne)




def afficher_infos_personne(numero_personne, nom, age: int):
  print("La personne " + str(numero_personne) + " est " + nom + " Son age est de "+ str(age) + "ans")
  print("Le nom comporte " + str(len(nom)) + " lettres")
  if est_majeur(age):
    print("Il est majeur")
  else:
    print("Il est mineur")

def récupérer_etafficher_infos_personnes(numero_personne):          #Pas besoin de plusieurs variables (nom1,ag1 ,nom22 ,age2)car les variables nom et ages sont 
  nom, age = recuperer_infos_personne(numero_personne)
  afficher_infos_personne(numero_personne, nom, age)
 

#récupérer_etafficher_infos_personnes(1)
#récupérer_etafficher_infos_personnes(2)
#récupérer_etafficher_infos_personnes(3)
numero_personne = 2
for i in range(numero_personne):              #De cette manière le programme peut s'adapter à un plus grand nombre de personnne
  récupérer_etafficher_infos_personnes(i+1)   #Il suffit de changer la valeur de la variable numero_personne et i ira jusqu'a cette nouvelle valeur
  afficher_infos_personne("OO7", "James", 40)

#définition de la fonction
#Dans une fonction quand il nous manque des informations comme ici le nom l'age et le nombre de lettre je les mets en paramètre

"""def afficher_infos_personne(nom="", age = 0): #<-paramètre infos manquantes
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
#->renvoyer une valeur(pas obligatoire)"""