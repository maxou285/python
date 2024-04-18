s = 1001; highest_num = s ** 2; n = 3; dia_sum = 1; increment = 2; count = 1

while n <= highest_num:
    dia_sum += n
    if count < 4: n += increment; count += 1
    else: increment += 2; count = 1; n += increment

print(dia_sum, increment-2)