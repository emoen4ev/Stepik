from fractions import Fraction


n = int(input())

num_1 = num_2 = Fraction(1, 1)

if n > 1:
    for num in range(2, n + 1):
        num_2 = num_1 + Fraction(1, num ** 2)
        num_1 = num_2

print(num_2)