# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
# 
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici : 
# https://codeavecjonathan.com/formations.html
#############################################################################
def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input("Votre réponse (entre "+str(min) + " et " + str(max)+ ") : ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR : Vous devez rentrer un nombre entre " + str(min) + " et " + str(max))
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min,max)


def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print(i+1,"-", choix[i])
    print()
    resultat_reponse_correcte = False
    reponse_int = demander_reponse_numerique_utilisateur(1,len(choix))
    if  choix[reponse_int-1].lower() == bonne_reponse.lower():                  # La fonction lower() sert à convertir toute la chaine en minuscule ici il faudrait aussi convertir
        print("Bonne réponse") 
        resultat_reponse_correcte = True                      # question[2] pour que cela fonctionne son opposé est upper()
    else:
        print("Mauvaise réponse")
        
    print()
    return resultat_reponse_correcte



def lancer_questionnaire(questionnaire):
    score_def = 0
    for question in questionnaire:
        if poser_question(question):
            score_def += 1
    return score_def


"""
    Questionnaire[]
        Question
            Titre : "Quelle est la capitale de la France ?"
            Réponses : ("Marseille"Nice","Paris","Nantes")
            bonne_reponse = "Paris
"""

#question1 = ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris")
#question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"),"Rome")

#questionnaire = [question1, question2]

questionnaire = (
    ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"),"Rome")
                )



score = lancer_questionnaire(questionnaire)


#poser_question(question1)
#poser_question(question2)

#poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score,"sur", len(questionnaire))
