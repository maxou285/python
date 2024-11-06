M = 51
row = [1, 1]
distinct = set([1])

for r in range(3, M + 1):
	newrow = [1]
	for i in range(0, len(row) - 1):
		newrow.append(row[i] + row[i + 1])
	newrow.append(1)
	row = newrow
	distinct |= set(row)

primesquares = [x**2 for x in range(2, M) if all(x % p != 0 for p in range(2, x))]

print("Result:", sum(n for n in distinct if all(n % p != 0 for p in primesquares)))