# Brute force
Sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i%5==0:                  # Si i = 0 (mod 3) ou i = 0 (mod 5)
        Sum += i
print(Sum)


# Beaucoup plus optimisé
#def sum_1_to_n(n):
#   return n * (n + 1) / 2
#
#def sum_multiples(limit, a):
#   return sum_1_to_n((limit - 1) // a) * a
#
#   print(sum_multiples(1000, 3) + sum_multiples(1000, 5) - sum_multiples(1000, 15))