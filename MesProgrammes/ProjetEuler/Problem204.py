
from math import log, sqrt

limit = 10 ** 9
type = 100

def primelist(limit):
	primes = [2]
	x = 3

	while x < limit:
		isprime = True
		s = sqrt(x)
		for p in primes:
			if p > s: break
			if x % p == 0:
				isprime = False
				break
		if isprime: primes.append(x)
		x += 2
	
	return primes

def recurse(limit, primes):
	if len(primes) == 0: return 1
	answer = 0
	p = primes[0]
	for i in range(int(log(limit, p)) + 1):
		answer += recurse(limit / p ** i, primes[1:])
	return answer
		
print(recurse(limit, primelist(type + 1)))