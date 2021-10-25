a = "n"
while a == "n":
  nbr = input("Rentrez un nombre : ")
  if nbr == "exit":
    exit(0)
  nbr = int(nbr)
  if nbr > 1:
    premier = True
    for i in range(2, int(nbr/2)):
      if (nbr % i) == 0:
        print("Ce nombre n'est pas premier")
        print(i)
        premier = False
        break
    if premier == True:
      print("Ce nombre est premier")
