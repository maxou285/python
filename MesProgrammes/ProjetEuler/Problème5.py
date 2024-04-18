"""Manière mathématique 

20 = 2^2 * 5
19 = 19
18 = 2 * 3^2
17 = 17
16 = 2^4
15 = 3 * 5
14 = 2 * 7
13 = 13
11 = 11


Donc 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560"""

import math
num = math.prod(range(2,21))
for i in range(2,21):
    while num%i == 0:
        for j in range(2,21):
            if((num//i)%j != 0):
                break
        else:
            num = num//i
            continue
        break

print(num)

