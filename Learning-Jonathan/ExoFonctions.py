#Tables de multiplications
#
#
#
#
#afficher_table_multiplication(n)
#min / max
#erreur si man > max

 
n = input("Quelle table souhaitez vous afficher ? ")




n = int(n)
def afficher_table_multiplication(n):
    min = 0
    max = 10
    for i in range(min,max):
        min = min + 1
        print(str(min) + " x " + str(n) + " = " + str(min * n))
        
    if min > max:
        return   
    
    



afficher_table_multiplication(n)




