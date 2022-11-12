# __str__ et __repr__

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    # représentation chaine
    # def __str__(self):
    #    return "STR"

    # dev pour débugger mais si la fonction __STR__ n'est pas présente le __repr__ fait aussi le trvail du __STR__ donc __REPR__ mieux sauf si on veut séparer les deux pour dev
    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)

personne1 = Personne("Jean", 20)
personne1.AfficherInfos()

print(personne1)
