for i in range(175,1000):
    sum = 1
    for chiffre in str(i):
        #print(chiffre)
        sum = sum*int(chiffre)
        #print(5*sum)
    if 5*sum==i:
        print("Found : " + str(i) )
        