nbr = input("Rentrez un nombre : ")
nbr = int(nbr)
if nbr > 1:
  for i in range(2, int(nbr/2)):
    if (nbr % i) == 0:
      print("Ce nombre n'est pas premier")
      break
  else:
     print("Ce nombre est premier")