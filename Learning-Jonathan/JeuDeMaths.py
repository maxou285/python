import random 


NOMBRE_MIN = 1                                                  #Grace à ce systeme de constantes le programme peut s'adapter très facilement
NOMBRE_MAX = 10                                                 #à toutes les valeurs on pourrait par exemple demander de choisir une difficulté
NB_QUESTIONS = 4                                                #qui modifierait uniquement les constantes et pas tout le programme (const ne se modif pas en prgm)


bon_point = False
nb_points = 0
erreur = False
operation = "ope"

nbr1 = 1
nbr2 = 1
operateur_str = "+"


def poser_question():
    try:                                                                    #Avec le block try et except on gère l'exception dans cet exercice ce n'était pas obligatoire
        global nbr1
        global nbr2
        global operateur_str
        global o
        nbr1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
        nbr2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
        o = random.randint(0,2)                                             #On peut interpréter les nombres aléatoires avec par exemple des conditions
        # 0 -> + 
        # 1 -> *
        operateur_str = "+"
        if o == 1:                                          
            operateur_str = "*"                                             #Grace à ces lignes on fait varier l'opérateur avec un random de nombres
        elif o == 2:
            operateur_str = "-"
        reponse = input("Calculez " + str(nbr1) + operateur_str + str(nbr2) + " = ")
        operation = ("Calculez " + str(nbr1) + operateur_str + str(nbr2) + " = ")
        repcorrecte = nbr1 + nbr2
        if o == 1:
            repcorrecte = nbr1 * nbr2
        if o == 2:
            repcorrecte = nbr1 - nbr2
        if int(reponse) == repcorrecte:
            return True
        else:
            return False
    except:
        print("ERREUR : Vous devez rentrer un nombre ") 
        return poser_question_erreur()
       
def poser_question_erreur():   
    try:                                                                    #Avec le block try et except on gère l'exception dans cet exercice ce n'était pas obligatoire
        reponse = input("Calculez " + str(nbr1) + operateur_str + str(nbr2) + " = ")
        operation = ("Calculez " + str(nbr1) + operateur_str + str(nbr2) + " = ")
        repcorrecte = nbr1 + nbr2
        if o == 1:
            repcorrecte = nbr1 * nbr2
        if o == 2:
            repcorrecte = nbr1 - nbr2
        if int(reponse) == repcorrecte:
            return True
        else:
            return False
    except:
        print("ERREUR : Vous devez rentrer un nombre ") 
        return poser_question_erreur()



# Programme principal


for i in range (0,NB_QUESTIONS):
    print("Question n° " , i+1 , "sur" , NB_QUESTIONS," : ")
    if poser_question():
      print("Réponse correcte ")
      nb_points += 1
    else:
        print("Réponse incorrecte ")
        
    


print("Score final : " + str(nb_points))

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent ")
elif nb_points == 0:
    print("Révisez vos maths")
elif nb_points < moyenne:
    print("Peut mieux faire ")
elif nb_points > moyenne:
    print("Pas mal ")
elif nb_points == moyenne:
    print("La moyenne")