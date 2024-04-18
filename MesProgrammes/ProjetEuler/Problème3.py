num=600851475143
for i in range (2,num):
    if i>(num**.5)+1:break
    while (num%i==0):
        num//=i
    if num!=1:
        max=num
    else : max=i
print ('max =', max)  