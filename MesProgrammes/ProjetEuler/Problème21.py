def divisors(n):
    result = list()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return sorted(result)


def sum_d(d):
    my_list = d[:-1]
    return sum(my_list)


b = 0
n_list = list()
for a in range(1, 10001):
    b = sum_d(divisors(a))
    temp = sum_d(divisors(b))
    if a == temp and a != b:
        n_list.append(b)
    else:
        continue

print(sum(n_list))