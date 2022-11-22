rows, cols = int(input()), int(input())

matrix = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i * j

for row in matrix:
    for col in row:
        print(str(col).ljust(3), end='')
    print()