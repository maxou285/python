"""fact = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
s = lambda n: sum(fact[c] for c in str(n))
print(sum(i for i in range(10, int(input("Quel nombre connard"))) if s(i)%i == 0))""" # version opti qui ne fonctionne pas



from math import factorial

f = [factorial(0),factorial(1),factorial(2),factorial(3),factorial(4),factorial(5), factorial(6), factorial(7),factorial(8),factorial(9)]
def facto_digits(n):
    s = 0
    while n:
        s += f[n%10]
        n //= 10

    return s

sol = 0             

for i in range(10, 10000000):
    if facto_digits(i) ==i:
        sol +=i

print(sol)