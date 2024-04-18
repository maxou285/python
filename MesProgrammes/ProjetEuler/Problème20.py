import math

answer = math.factorial(100)

final_answer = sum(int(digit) for digit in str(answer))
print(final_answer)