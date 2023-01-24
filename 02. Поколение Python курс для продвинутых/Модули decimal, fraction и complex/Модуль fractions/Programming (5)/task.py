from fractions import Fraction as Fr
from math import factorial as f


n = int(input())

result = sum([Fr(1, f(i)) for i in range(1, n + 1)])

print(result)