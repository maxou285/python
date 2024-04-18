def isprime(z):
    for n in range(2,int(z**0.5)+1):
        if z%n==0:
            return False
    return True

n = 0
primesmax = [0,0,0]

for a in range(-999,1000):
  for b in range(-1000,1001):
    check = True
    n = 0
    while check:
      num = n**2 + a*n + b
      check == False
      if isprime(abs(num)):
        check == True
        n += 1
      else:
        break
    if primesmax[0] < n:
      primesmax = [n,a,b]

print(primesmax[1]*primesmax[2])