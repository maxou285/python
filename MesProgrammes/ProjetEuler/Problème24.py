
import math


n = 10    # n le nombre d'éléments
elements = [i for i in range(n)]
m = 1000000     


permutation = []
i = n
while True:
    s = math.factorial(i - 1)
    q = m // s
    r = m % s
    if r > 0:
        permutation.append(elements[q])
        elements.pop(q)
    else:
        permutation.append(elements[q - 1])
        elements.pop(q - 1)
        break
    m = r
    i -= 1
permutation.extend(list(reversed(elements)))


print(''.join([str(i) for i in permutation]))