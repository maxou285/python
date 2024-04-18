def ezbitch():
    n_1=(0,3,3,5,4,4,3,5,5,4)                   #1 à 9
    n_10=(0,3,6,6,5,5,5,7,6,6)                  #10 à 90
    n_11=(0,6,6,8,8,7,7,9,8,8)                  #11 à 19
    n=(7,10,11)                                 #centaine(hundred) centaine et (hundred and... (hundrer and fifty-six)) millier(thousand)
    
    first_hundred = (sum(n_1)*9 + n_10[1] +sum(n_11) + sum(n_10[2:])*10)*10
    n100_a_900 = n[0]*9 + n[1]*99*9+sum(n_1)*100

    nbrlettres = first_hundred + n100_a_900 + n[2]
    return nbrlettres
print(ezbitch())