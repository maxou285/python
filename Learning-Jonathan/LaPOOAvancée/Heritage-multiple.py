# HERITAGE MULTIPLE : MULTIPLE-INHERITANCE

class EtreVivant:
    def afficher_infos(self):
        print("Je suis un être vivant")

class Predateur():                                      
    def chasser_et_manger_proie(self):
        print("miam miam")

class Lion(EtreVivant, Predateur):          # on peut aussi faire hériter prédateur de etre vivant et enlever l'héritage etre vivant ici
    def afficher_infos(self):
        print("Je suis un lion")

class Personne(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")

lion = Lion()
lion.afficher_infos()
lion.chasser_et_manger_proie()
