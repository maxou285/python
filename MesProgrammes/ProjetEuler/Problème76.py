NMAX = 100
ways = []
def possibilities():
    ways = [1] + [0] * NMAX
    print(ways)
    for i in range(1,NMAX):
        for x in range(i,len(ways)):
            ways[x] += ways[x-i]
    print(ways[-1])

possibilities()