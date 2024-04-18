def reste(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n**0.5+1),2):
        index = i*2
        while index <n:
            is_prime[index] = False
            index = index+i
    
    prime = [2]
    for i in range(3,n,2):
        if is_prime[i]:
            prime.append(i)
    return prime


primes = reste(1000000)

solution = []


for prime in primes:
    correct = True
    number = prime
    mul = 10**(len(str(number))-1)
    number = (number-(number/mul)*mul)/10

    while number:
        if (number%10) %2 == 0 or (number%10)%5 == 0:
            correct = False
            break
        number = number/10

    if correct:
        number = prime/10
        solution.append(prime)
        while number:
            if number not in primes:
                solution.remove(prime)
                break
            number //=10

sol = solution[4:]
for i in sol:
    number = i
    while number:
        mul = 10**(len(str(number))-1)
        number = number-(number/mul)*mul
        if number not in primes and number != 0:
            solution.remove(i)
            break

print(sum(solution))