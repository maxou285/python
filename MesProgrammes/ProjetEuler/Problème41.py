from math import sqrt

is_prime = lambda x: all(x % i != 0 for i in range(2, int(sqrt(x)) + 1))
is_pandigital = lambda x: sorted(str(x)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:len(str(x))]

for x in range(9999999, 1, -1):
	if is_pandigital(x) and is_prime(x):
		print(x)
		break