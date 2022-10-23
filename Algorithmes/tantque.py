#! /usr/bin/python3

A=input("Entre un nombre ? ")
A=int(A)
resultat=A

while (A != 0):
    A=input("Entre un nombre ? ")
    A=int(A)
    resultat = resultat + A
print("Le résultat de la somme est : " + str(resultat))