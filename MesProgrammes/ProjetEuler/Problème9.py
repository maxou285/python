import math
import time


def is_integer(number):
    return int(number) == number


def special_pythagorean_triplet(number):
    start_time = time.time()
    # a<b<c
    amax = int(number / 3)# - 1 + 1
    bmax = int((number - 2) / 2) + 1

    for a in range(1, amax + 1):
        for b in range(a + 1, bmax + 1):
            sqr_sum = a ** 2 + b ** 2
            c = math.sqrt(sqr_sum)

            if is_integer(c) and a + b + c == number:
                print("Time taken:", "{:.4f}".format(time.time()-start_time), "seconds")
                print(a, b, int(c))
                return a * b * int(c)


print(special_pythagorean_triplet(1000))