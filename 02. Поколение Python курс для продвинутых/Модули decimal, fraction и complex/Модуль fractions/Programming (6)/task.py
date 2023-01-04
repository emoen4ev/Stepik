from fractions import Fraction as Fr
from decimal import Decimal


n = int(input())

sequence = list()

for num in range(1, n // 2):
    cur_num = num / (n - num)
    sequence.append(cur_num)


result = Fr(str(max(sequence)))
print(result)