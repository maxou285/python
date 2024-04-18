import math
def sum(num):
    sums = 0
    while num>9:
        sums+=num % 10
        num = int(num/10)
        return sum
    
print(sum(math.pow(2,1000)))
