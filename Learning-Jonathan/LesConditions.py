age = input("Quel est votre age ?" )
age = int(age)
if age < 18: 
  print(" Vous etes mineur")
elif age > 18: 
  print("Vous etes Majeur")
elif age == 18: 
  print("Félicitations, vous etes tout juste majeur")
if age > 70:
  print("Vous etes senior ")
if age < 10: 
  print("Vous etes enfant")
elif age >= 12 and age <18: 
  print("Vous etes adolescent")
if age == 1 or age == 2:
  print("Vous etes un bébé")
else:
  print("Incorrect")