
from math import sqrt,ceil,floor
def rect(m,n):
    return m+n+2*m*n+1
Sqr=[]
big=5000000
ind=0
def mkSqr(limit):
    global Sqr
    Sqr.append(((int(limit))**2,int(limit)))
    for i in range(limit-1,max(limit-big,-1),-1):
        Sqr.append((Sqr[-1][0]-(i<<1)-1,i))
def sqr(val):
    if val<=Sqr[-1][0]:
        return int(ceil(sqrt(val)))
    global ind
    while val<=Sqr[ind][0]:
        ind+=1
    return Sqr[ind-1][1]
def circ(r):
    ret=0
    rs2=r*r*2
    limit=int(ceil((sqrt(rs2))))
    mkSqr(limit)
    n=0
    for i in range(1,limit):
        n+=((i-1)<<1)+1
        #ret+=int(ceil(sqrt(rs2-i*i)))
        ret+=sqr(rs2-n)
    return ret*4-2*(r-1)
def howmany(r):
    return rect(r,r/2)+rect(r,r/4)-2*(r+1)-r/2-r/4+circ(r/8)

print(howmany(1000000000))