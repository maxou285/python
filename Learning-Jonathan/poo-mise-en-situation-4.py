# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom
        
    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)


# ---
noms = []
    
for i in range(0, 3):
    noms.append(input("nom de la personne " + str(i+1) + " : "))
    
liste_personnes = []


for nom in noms:
    liste_personnes.append(Personne(nom))

for personne in liste_personnes:
    personne.SePresenter()