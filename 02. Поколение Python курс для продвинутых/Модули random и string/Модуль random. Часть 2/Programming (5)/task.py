import random

ll = random.sample(range(1, 76), 25)

matrix = [ll[i:i + 5] for i in range(0, len(ll), 5)]

matrix[2][2] = 0

for row in matrix:
    for col in row:
        print(str(col).ljust(3), end='')
    print()