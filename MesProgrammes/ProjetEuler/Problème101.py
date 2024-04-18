# Méthode d'interpolation de Lagrange
Facto=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800]

def Combi(n,k):
    return Facto[n]//(Facto[k]*Facto[n-k])

#On calcule les valeurs de u_n pour n allant de 1 à 11
#et on mets dans la liste Termes en ajoutant un 1 au début
#pour que le 1er terme de la liste ait pour indice 1

def polynome(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

Termes=[1]
for i in range(10):
    Termes.append(polynome(i+1))
    
#On note BOP(k)  ce qui était noté OP(k,k+1)
#et on le calcule à l'aide de la formule trouvée ci-dessus
#et la méthode d'interpolation Lagrangienne
def BOP(k):
    r=0
    for j in range(1,k+1):
        r+=Termes[j]*(-1)**(k-j)*Combi(k,j-1)
    return r

#on somme BOP(k) pour k allant de 1 à 10
resultat=0
for i in range(1,11):
    resultat+=BOP(i)
print(resultat)