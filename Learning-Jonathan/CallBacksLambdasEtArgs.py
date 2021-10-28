# Fonctions Avancées
#
# CALLBACK
#
#



"""def ma_fonction():
    print("toto")
    return 1

a = 5



b = ma_fonction                 # En ne mettant pas le parenthèses b devient ma_fonction c'est pour cela que l'on peut appeller b() et que le résultat 
                                # est le meme que si on avait appellé ma_fonction()
print("a", a ,"b" , b())"""




def afficher_table(n, operateur_str, operation_cbk):                # Grace aux callbacks je peux stocker une fonction dans une variable et ainsi pouvoir 
    for i in range(1,10):                                           # faire évoluer mon code très facilement 
        print(i,operateur_str,n,"=",operation_cbk(i,n))

def mult_callback(a,b):                                             # Ici la variable operation_callback appel les fonctions données pour concaténer 
    return a*b                                                      # l'opérateur c'est un exemple simple mais les callbacks peuvent etre très utiles

def add_callback(a,b):
    return a+b

def power_callback(a,b):
    return pow(a,b)

# Fonctions LAMBDA
#
# Les fonctions LAMBDA sont des fonctions que l'on ne définis pas auparavant on les définis dans le code au moment ou on a besoin de s'en servir
#  
# On defini la fonction après le mot clé lambda
#


afficher_table(2, "x",lambda a,b : a*b)
print()
afficher_table(2, "+",add_callback)
print()
afficher_table(2, "^",power_callback)



# Nombre variable de paramètres
# 
# Utiles si on ne connait pas à l'avance le nombre de paramètres qu'aura une fonction par exemple une moyenne de note mais on  ne connait pas le nombre
# de notes

def somme(titre, *nombres):                 # *nombres sert si on ne connait pas à l'avance le nombre de nombres 
    print("Titre : " , titre)               # **nombres si on veut donner une clé par exemple : 
    resultat = 0                            # def somme(titre, **nombre)
    for n in nombres:                       # print("Titre : " , titre)  
        resultat += n                       # resultat = 0
    return resultat                         # for n in nombres:
                                            # return resultat   

print(somme(2,5,4))                         # print(somme(maths = 15,Géo = 11, Anglais = 18))
