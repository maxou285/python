# PROGRAMMATION ORIENTÉE OBJET 
# Un objet est une instance de classe 
# par exemple objet oeuf est une instance de la classe Oeuf


# Personne (Entité -> Class)
#   Données : nom age
#   Actions : (méthodes)
#       - Se présenter ()
#       - DemanderNom() / input

# -----DÉFINITION-----



class Personne:
    def __init__(self, nom = "", age = 0):
        self.nom = nom               # Crée une variable d'instance : nom
        self.age = age               # Crée une variable d'instance : age
        print("Constructeur personne " + self.nom)
        if self.nom == "":
            self.Demander_nom()
           
        
        


    def SePresenter(self):
        if self.age == 0:
            print("Bonjour je m'appelle " + self.nom)
        else:
            print("Bonjour je m'appelle " + self.nom + " j'ai " + str(self.age) + " ans ")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        if self.age >= 18:
            return True
        return False


    def Demander_nom(self):
        self.nom = input("Quel est votre nom ? ")
        return self.nom

   
# -----UTILISATION-----

personne1 = Personne("Jean",30) 
personne2 = Personne("Paul",15)             # Je crée une personne

liste_personnes = [personne1, personne2, Personne()]



#personne3 = Personne()
personne4 = Personne(age = 20)



print("Affichage list 1 ")

for personne in liste_personnes:
    personne.SePresenter()




liste_personnes.append(personne4)

print("Affichage list 2 ")


for personne in liste_personnes:
    personne.SePresenter()



#personne1.SePresenter()
#personne2.SePresenter()
#personne3.SePresenter()
#personne4.SePresenter()

#print("EstMajeur1 : " + str(personne1.EstMajeur()))
#print("EstMajeur2 : " + str(personne2.EstMajeur()))

#print("Nom1 : " + personne1.nom)
# personne2.AutreFonction()               # Méthode d'instance    -> quand on travaille sur un objet (avec le self)

# Personne.SePresenter(personne1)        # Méthode de Classe
# personne2 = Personne("Paul")              # Je crée une 2e personne



"""def afficher_informations_personne(nom,age):
    print("La personne s'appelle " , nom , "son age est ", age,"ans")


def demander_nom_personne():
    nom = input("Quel est votre nom  ?")
    return nom
nom1 = "Jean"
age1 = 30


nom2 = "Paul"
age2 = 25

afficher_informations_personne(nom1,age1)
afficher_informations_personne(nom2,age2)
nom3 = demander_nom_personne()
age3 = 18
afficher_informations_personne(nom3,age3)"""

