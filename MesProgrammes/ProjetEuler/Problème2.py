n1 = 1
n2 = 2
n = 0
Sum = n1 + n2
while n < 4000000:
    n = n1 + n2
    Sum += n
    n1 = n2
    n2 = n
    print(n)
print(Sum-n)                        # le dernier n dépasse 4 000 000
    