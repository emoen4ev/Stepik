from fractions import Fraction as Fr


n = int(input())

sequence = set()

for num in range(1, n // 2 + 1):
    cur_num = Fr(num, n - num)

    if cur_num.numerator + cur_num.denominator == n:
        sequence.add(cur_num)

largest = max(sequence)

print(largest)