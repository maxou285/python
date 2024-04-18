L = [1,2,3,4,5,6,7,8]


import itertools
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
        
permutation = list(itertools.permutations(L))
#print(permutation)
N = 0
for i in permutation:
    print(i)
    if i[0]==i[1]-1 or i[1]==i[2]-1 or i[2]==i[3]-1 or i[3]==i[4]-1 or i[4]==i[5]-1 or i[5]==i[6]-1 or i[6]==i[7]-1:
        N = N+1

print(N)
