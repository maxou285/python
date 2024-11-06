import math

nmax = 64000000

div = nmax * [1]

for x in range(2, len(div)):
    if div[x] == 1:
        for y in range(x, len(div), x):
            a,b,z = 1,1,y
            while z % x == 0:
                z //= x
                b *= x
                a += b ** 2
            div[y] *= a

print(sum(x for x in range(1, len(div)) if div[x] == int(math.sqrt(div[x])) ** 2))