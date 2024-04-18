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

compteur = 0

for i in primes:
    correct = True
    number = i/10

    while number:
        if (number%10) %2 == 0 or (number%10)%5 == 0:
            correct = False
            break
        number //= 10

    if correct:
        lenght = len(str(i))
        number = i
        compteur += 1
        for j in range(lenght):
            number = (number%10)*10**(lenght-1) + number//10
            if number not in primes:
                compteur -=1
                break

print(compteur)