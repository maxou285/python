from random import *

def joue(difficulte,valeurmax):
  if difficulte == "difficile":
    print("Dans la difficulté difficile le nombre à trouver est compris entre 1 et 1000 mais Attention car cette fois tu n'as le droit qu'a 10 tentatives")
    tentatives = 10
  else:
   print("Dans la difficulté "+difficulte+" le nombre à trouver est compris entre 1 et "+str(valeurmax))
  f = randint(1, valeurmax)
  win = False
  while win == False:
    d = input("Entre un nombre : ")
    d = int(d)
    if d < f:
      print("Plus ! ")
    elif d > f:
      print("Moins ! ")
    elif d == f:
      win = True
      print("Bien joué tu as trouvé ! ")
      break
    if difficulte=="difficile":
      tentatives = tentatives-1
      print("Tu n'as plus que "+ str(tentatives) + " tentatives")

print("Bonjour, Bienvenue dans mon jeu Devine le nombre ")
a = input("Choisis une difficulté entre facile, medium ou difficile ")
win = False
if a == "facile":
  joue(a,50)
elif a == "medium":
  joue(a,100)
elif a == "difficile":
  joue(a,1000)

