mxp = 918273645
products = []
largest_pandigital = 0
for i in range(9, 9999):
    digits = []
    for j in range(1, 3):
        k = str(i * j)
        for d in k:
            if d == "0":
                digits = []
                break
            digits.append(d)
            if digits.count(d) > 1:
                digits = []
                break
    if len(digits) == 9:
        n = ""
        for d in digits:
            n += d
        if int(n) > largest_pandigital:
            largest_pandigital = int(n)
print(largest_pandigital)