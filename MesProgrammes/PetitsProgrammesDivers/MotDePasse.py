password = ""
tentatives = 3
while password != "gentil":
  password = input("Rentrez un mot de passe ")
  tentatives = tentatives - 1
  if password == "gentil":   
    print("Mot de passe correct vous avez accès à vos données")
    break
  if tentatives > 0:
    if password == "":
      print("Vous devez rentrez un mot de passe")
      print("Mot de passe incorrect, veuillez réessayer il vous reste encore " + str(tentatives) + " essais ")
    else:
      print("Mot de passe incorrect, veuillez réessayer il vous reste encore " + str(tentatives) + " essais ")
  if tentatives == 0:
      print("Plus de tentatives veuillez réessayer plus tard")
      break


   #Les breaks ne servent à rien car de toutes facons on ne rentrera pas dans le code qui suit