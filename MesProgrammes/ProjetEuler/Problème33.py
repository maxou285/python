def pgcd(a,b):
    b,a = min((a,b)), max((a,b))
    if a%b == 0:
        return b
    
    sreste = (a|b)%2
    h = 1
    for j in range(2+sreste, b//2 +1, 1+sreste):
        # On check j
        if b%j ==0 and a%j == 0: 
            h = j   
    return h

numerator = 1
denominator = 1
for i in range(1,10):
    for d in range(1,i):            # d reste au dénominateur
        for n in range(1,d):        # n reste au numérateur
            if 10*d*n + i*d == 10*i*n + d*n:
                numerator = numerator*(10*n + i)
                denominator = denominator*(10*i + d)

common_term = pgcd(numerator,denominator)

print(denominator//common_term)         