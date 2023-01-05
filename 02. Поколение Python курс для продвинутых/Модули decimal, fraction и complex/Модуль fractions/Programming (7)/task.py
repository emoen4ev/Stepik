from fractions import Fraction


n = int(input())

result = set()

for i in range(1, n):
    for j in range(i + 1, n + 1):
        result.add(Fraction(i, j))

result = sorted(result)

print(*result, sep="\n")