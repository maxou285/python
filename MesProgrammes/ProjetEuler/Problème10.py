number=2000000
primesum = 0

is_prime = [True for _ in range(number+1)]
is_prime[0], is_prime[1] = False, False #préciser 0 and 1 not primes

for i in range(2, int(number**0.5)+1):
  if is_prime[i]:
    for j in range(i*i, number+1, i):
      is_prime[j] = False
for i in range(2, number+1):
  if is_prime[i]:
    primesum += i

print("Sum of prime numbers from 1 to", number, "is", primesum)

"L'algorythme d'Erathosthène"