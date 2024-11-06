import math

i,k=1,0
while True: 
 i*=2
 k+=1
 if k*1./(i-1)<1./12345.:
  k-=1
  i=12345*k + 2
  print(i*(i-1))
  break