from sympy import sieve

N = 40_000_000
phi = [0] + list(sieve.totientrange(0, N))

for n in range(2, N):
    phi[n] = 1 + phi[phi[n]]

answer = 0
for p in sieve.primerange(0, N):
    if phi[p] == 25:
        answer += p

print(answer)