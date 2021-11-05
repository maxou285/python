class Question:
    def __init__(self,question, reponse, nb_question):
        self.question = question
        self.reponse = reponse
        self.nb_question = nb_question

    def poser_question(self):
        print()
        print("  QUESTION numero "+ str(self.nb_question+1) + " : " + self.question)
        for i in range(0,4):
            print(str(i+1) + " - " + str(liste_reponses[self.nb_question][i]))
            i += 1
        self.reponse = input("  Votre réponse : ")

    def verifier_reponse(self):
        global score
        try:
            if self.reponse == "" :
                print("ERREUR : Veuillez rentrer une réponse valide ")
                while self.reponse == "":
                    Question.verif_except()
                    return
       
            if int(self.reponse) > 4:
                print("ERREUR : Veuillez rentrer une réponse comprise entre 1 et 4 ")
                while int(self.reponse) > 4:
                    Question.verif_except()
                    return
            if int(self.reponse) < 1:
                print("ERREUR : Veuillez rentrer une réponse comprise entre 1 et 4")
                while int(self.reponse) < 1:
                    Question.verif_except()
                    return
        except:
            pass
        if  self.reponse.lower() == bonne_reponse[self.nb_question].lower():
            print("Reponse correcte ")
            return True
        elif self.reponse.lower() == str(bonne_reponse_int[self.nb_question]):
            print("Reponse correcte ")
            return True
        else:
            print("Reponse incorrecte ")
        return
        
        
    def verif_except():
        global score
        i.poser_question()
        if i.verifier_reponse():
            score = score + 1

            ### Reposer la question 

bonne_reponse_int = [3,1,4]     
bonne_reponse = ["Paris", "Rome", "Bruxelles"]
score = 0
nb_totale_questions = 3


question1 = Question("Quelle est la capitale de la France ? ","Paris ",0)
question2 = Question("Quelle est la capitale de l'Italie ? ","Rome ",1)    
question3 = Question("Quelle est la capitale de la Belgique ? ","Bruxelles",2)       

liste_question = [question1, question2, question3]
    #("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris"),
    #("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"),"Rome")
liste_reponses = (("Marseille","Nice","Paris","Nantes"),
                 ("Rome", "Venise", "Pise", "Florence"),
                 ("Anvers", "Andenne", "Louvain", "Bruxelles")
                 )                   


                     




for i in liste_question:
    i.poser_question()
    if i.verifier_reponse():
        score = score + 1


print(" Score final : " + str(score))
if score == nb_totale_questions:
    print("---Excellent !--- ")
elif score == 0:
    print("---Revisez votre géographie--- ")
elif score > nb_totale_questions/2:
    print("---Pas mal---")
elif score < nb_totale_questions/2 and score != 0:
    print("---Peu mieux faire--- ")

    