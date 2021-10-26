# LES FONCTIONS:PROJET QUESTIONNAIRE
#
# Question: Quelle est la capitale de la France ? 
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse : 
# Bonne réponse / mauvaise réponse
#
# ...
# Question: Quelle est la capitale de l'Italie? 
# ...
#
# 4 questions

def questions(ville1,ville2,ville3,ville4,pays,bonne_reponse):
    global score                                                    # On met la variable score en global car sinon le prgm principal ne peut pas la lire elle est locale
    print()
    print("Quelle est la capitale de " + pays + "? ")
    print()
    print("(a)", ville1)
    print("(b) ",ville2)
    print("(c) ",ville3)
    print("(d) ", ville4)
    print()
    reponse = input("Votre réponse : ")
    
    if reponse == bonne_reponse:
        print("Bonne réponse")
        score +=1
    else:
        print("Mauvaise réponse")
       

score = 0

questions("Marseille", "Nice" , "Paris", "Nantes", " la France","c")
questions("Florence", "Rome" , "Venise", "Naples", "l'Italie","b")
questions("Kaboul", "Hérat" , "Khost", "Baglan", "Afghanistan","a")
questions("Lagos", "Porto" , "Lisbonne", "Madrid", "Portugal","c")

print("Score final : " + str(score))