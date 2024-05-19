def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k
      return F
   
print(factorielle(4))
sum = 0
for i in range(1,31):
   sum += factorielle(i)
   print(i)
   print(sum)