# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# FONCTIONS RÉCURSIVES                      Une fonction récursive est utilisé quand on veut forcer l'utilisateur par exemple dans ce cas à donner un choix valide
'''def a(n, limit):                          Le principe des fonctions récursives est que l'on peut les appeller dans leur def pour une certaine condition
    if n > limit:
        return
    print("n:", n)
    a(n*n, limit)

a(2, 100000)'''

def demander_choix_utilisateur(min, max):
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + " :")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("ERREUR: Vous devez rentrer un nombre entre", min, " et ", max)       # Vérifier que l'utilisateur donne bien un nombre entre 1 et 4
            return demander_choix_utilisateur(min, max)                                 # Ici on utilise la récursivité on rappelle la fonction tant 
        return reponse_int                                                              # que l'utilisateur n'as pas donné un choix valide 
    except:
        print("ERREUR: Vous devez rentrer un nombre")                                      #On traite les cas d'erreur et repose la question
        return demander_choix_utilisateur(min, max)


choix = demander_choix_utilisateur(1, 4)
print("Choix de l'utilisateur:", choix)