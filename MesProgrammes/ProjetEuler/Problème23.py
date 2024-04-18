divisors_sum = [sum(d) for d in [[j for j in range(1, i) if i % j == 0] for i in range(28124)]]
abundants = [[i, d] for i, d in enumerate(divisors_sum) if d > i]

abundants_sum = set()
for i, a in enumerate(abundants):
    for j, b in enumerate(abundants[i:]):
        abundants_sum.add(a[0] + b[0])

non_abundants_sum = [i for i in range(1, 28124) if i not in abundants_sum]
print(sum(non_abundants_sum))