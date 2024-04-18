number = "0."          

add_number = 1

while len(number) < 1000002:
    number += str(add_number)
    add_number += 1

multiples = 1

for i in range(7):
    multiples *= int(number[10 ** i + 1])

print(multiples)