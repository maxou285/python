
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    def Afficher(self):
        if self.vegetarienne == True:
            print("PIZZA " + self.nom + " : " + str(self.prix) + " €" " - VEGETARIENNE") 
            print(", " .join(self.ingredients))
            print()
        else:
            print("PIZZA " + self.nom + " : " + str(self.prix) + " €")
            print(", " .join(self.ingredients))
            print()
       
    
class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1                  # Variable globale à toutes les classes 
        self.nb_pizzas = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisee "+ str(self.nb_pizzas), 0, [])
        self.Demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def Demander_ingredients_utilisateur(self):
        print()
        print("Ingrédients pour la pizza personnalisée numero", self.nb_pizzas)
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print("Vous avez " + str(len(self.ingredients)) + " ingredient(s) : " + ' ,'.join(self.ingredients))

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + self.PRIX_PAR_INGREDIENT*len(self.ingredients)
 

pizza1 = Pizza("4 fromages", 8.50, ("brie","emmental", "compté", "parmesan"), vegetarienne = True)


pizza2 = Pizza("Hawai", 6.70, ("Tomates","ananas", "oignons"))


pizza3 = Pizza("La spéciale", 12, ("Champignons","lavande", "oranges", "gruière rapé", "Tomates"), vegetarienne = True)



pizzas = [pizza1, pizza2, pizza3, PizzaPersonnalisee(), PizzaPersonnalisee()]

def tri(element):
    return len(element.ingredients)


pizzas.sort(key = tri, reverse = True)

for i in pizzas:                # Afficher uniquement les pizzas vegetariennes
    i.Afficher()


    
