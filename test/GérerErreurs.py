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

demander_reponse_numerique_utilisateur(1,10)