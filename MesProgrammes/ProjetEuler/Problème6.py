def sumofsquares(n):
    return (n/6)*(n+1)*((2*n)+1)

def squareofsum(n):
    return ((n**2 + n) / 2) ** 2

print("Difference: " +  str(squareofsum(100) - (sumofsquares(100))) )