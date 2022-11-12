# Méthodes d’instance, de classe et statiques

class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom

    # Méthode d'instance 99% des cas
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)

    # premier charactère en majuscule puis minuscules
    # méthode statique de tant en tant
    @staticmethod                           # pour pouvoir l'appeller depuis une instance sans qu'il y ait de problèmes car self manquant
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()
        #return Personne.TYPE
    
    # méthode de class très très rarement utilisé
    @classmethod
    def methode_de_classe(cls):             # avoir accès à la classe grace au paramètre cls
        print("Méthode de classe : " + cls.TYPE)

# en pratique @classmethod est très peu utilisé car @staticmethod peut déja accéder à la classe avec Personne.TYPE par exemple

personne1 = Personne("jean")
personne1.se_presenter()

print(Personne.formater_chaine("toTo"))

Personne.methode_de_classe()