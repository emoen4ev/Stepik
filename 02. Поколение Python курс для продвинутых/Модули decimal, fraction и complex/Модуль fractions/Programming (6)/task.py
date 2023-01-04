from fractions import Fraction as Fr
from decimal import Decimal


n = int(input())

sequence = list()

for num in range(1, n // 2):
    cur_num = Fr(num, n - num)
    sequence.append(cur_num)

sequence.sort(reverse=True)
largest = max(sequence)
sequence_2 = [str(x) for x in sequence]
largest_2 = max(sequence_2)
print(*sequence)
print(sequence_2)
print(largest)
print(largest_2)