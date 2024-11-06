"""lp = [1]
n = int(input("pour n = "))
k = int(input("pour k = "))
for j in range(n):
    nl = lp + [1]
    for i in range(len(lp) - 1):
        nl[i + 1] = lp[i] + lp[i + 1]
    lp = nl
print(nl[k])
"""
from math import factorial

# input n
n = 82
for i in range(n):
    for j in range(n-i+1):

        # for left spacing
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/((n-r)!*r!)
        print((factorial(i)//(factorial(j)*factorial(i-j)))%2, end=" ")

    # for new line
    print()