from math import sqrt

def penta_gen(maxnum):
    i = 1
    while (i*((3*i)-1))/2 <= maxnum:
        yield (i*((3*i)-1))/2
        i += 1

def isPenta(Pn):
    num = (1 + sqrt(1 + 24*Pn))/6.0
    if num == int(num):
        return True
    return False

for index,x in enumerate(penta_gen(100000000)):
    if index%100==0: print(index, x)
    for y in penta_gen(x/2):
        if isPenta(x-y):
            if isPenta(x-2*y):
                break
    else:
        continue
    break
print(x-2*y)