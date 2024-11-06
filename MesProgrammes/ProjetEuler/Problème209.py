import functools, operator

s = 64 * [True]
c = []

for i in range(64):
    n = 0
    j = i
    while s[j]:
        s[j] = False
        n += 1
        j = j // 2 + (32 if j % 8 in (1, 3, 5, 6) else 0)
    if n:
        c.append(n)

print(c)

f = [1,2] + 63 * [0]
for i in range(2, len(f)):
    f[i] = f[i-1] + f[i-2]

print(functools.reduce(operator.mul,(f[i-1] + (0 if i < 2 else 1 if i < 3 else f[i-3]) for i in c), 1))