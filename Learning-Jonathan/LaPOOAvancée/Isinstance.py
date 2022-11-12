# IsInstance : Vérifier les types

class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

        if not isinstance(age, int):            # à la place de int on peut passer n'importe laquelle de nos classes (int est une classe à la base)
            print("L'age doit être de type int")
            self.age = 0

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}")
        if self.age > 0:
            print(f"L'an prochain j'aurai {self.age+1} ans")


personne = Personne("Jean", "20")
personne.AfficherInfos()

