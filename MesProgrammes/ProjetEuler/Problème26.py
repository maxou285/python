max=0
for i in range(2,1000):
    r=[];j=1
    #on cherche le premier reste de la division dejà rencontré: la période s'arrete là
    while 10**(j-1)%i not in r:
        r.append(10**(j-1)%i)     
        j=j+1
    if len(r)>max: max=len(r);imax=i
print(max,imax)