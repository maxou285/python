def dice(x,n,s):
    sum=0
    for k in range(0, int((s-x)/n+1)):
        sum+=((-1)**k)*c(x,k)*c(s-(n*k)-1,x-1)
    return sum

def c(a,b):
    if b==0:
        return 1
    else:
        return (fac(a))/(fac(b)*fac(a-b))

def fac(a):
    if a<=1:
        return 1
    else:
        return a*fac(a-1)

a=[dice(9,4,i) for i in range(0,37)]
b=[dice(6,6,i) for i in range(0,37)]
sum=0
for i in range(0,len(a)):
    for k in b[:i]:
        sum+=a[i]*k
print(sum*1.0/(4**9*6**6))