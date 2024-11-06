def f():
    s = 55 * [0]
    for k in range(55):
        s[k] = (100003 - 200003 * (k + 1) + 300007 * (k + 1) ** 3) % 1000000
        yield s[k]
    while True:
        s[:-1], s[-1] = s[1:], (s[-24] + s[-55]) % 1000000
        yield s[-1]

n = 50000
c = []

for x, y, z, d, e, f in zip(*[iter(f())]*6):
    c.append((x % 10000, y % 10000, z % 10000,
              1 + d % 399, 1 + e % 399, 1 + f % 399))
    if len(c) == n:
        break

def sweep(x, f):
    q = sorted([(f(i)[0], 1, i) for i in x] +
                [(f(i)[1], 0, i) for i in x] + [(10401, 2, -1)])
    s = set()
    i = 0
    while q[i][1] != 2:
        x = q[i][0]
        while q[i][0] == x and q[i][1] == 0:
            s.remove(q[i][2])
            i += 1
        while q[i][0] == x and q[i][1] == 1:
            s.add(q[i][2])
            i += 1
        yield q[i][0] - x, s

v = 0

for x in sweep(range(len(c)), lambda i: (c[i][0], c[i][0] + c[i][3])):
    for y in sweep(x[1], lambda i: (c[i][1], c[i][1] + c[i][4])):
        for z in sweep(y[1], lambda i: (c[i][2], c[i][2] + c[i][5])):
            if z[1]:
                v += x[0] * y[0] * z[0]

print(v)