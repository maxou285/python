#! /usr/bin/python3

prenom=input("Comment t'appelles tu ? ")
age=input("Quel age as tu ? ")
print("Salut "+ prenom + " tu as " + age + " ans ! ")
print(type(prenom))
print(type(age))

A=input("Entre un premier nombre ? ")
B=input("Entre un deuxième nombre ? ")
C=A+B
print(C)
print(type(C))

A=int(A)        # transforme la chaine de caractere en entier pour que je fasse des calculs
B=int(B)        # transforme la chaine de caractere en entier pour que je fasse des calculs
C=A+B
print(C)
print(type(C))
