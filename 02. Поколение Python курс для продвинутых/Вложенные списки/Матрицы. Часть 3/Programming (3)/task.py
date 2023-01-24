rows, cols = [int(_) for _ in input().split()]

size = rows * cols

matrix = [[row + col for col in range(0, size, rows)] for row in range(1, rows + 1)]

for row in matrix:
    print(''.join(str(x).ljust(3) for x in row))