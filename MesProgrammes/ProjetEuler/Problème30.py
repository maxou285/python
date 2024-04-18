sum1, sum2 = 0, 0
for i in range(10, 999999):
    number = i
    sum1 = 0
    while number != 0:
        digit = number % 10
        sum1 += digit**5
        number //= 10
    if i == sum1:
        sum2 += i
print(sum2)