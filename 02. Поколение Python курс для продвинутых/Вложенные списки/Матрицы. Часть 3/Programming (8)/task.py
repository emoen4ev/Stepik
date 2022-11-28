rows, cols = [int(_) for _ in input().split()]

matrix = [[1] * cols for _ in range(rows)]

counter = 0

for k in range(rows * cols):
    for i in range(rows):
        for j in range(cols):
            if i + j == k:
                counter += 1
                matrix[i][j] = counter

for row in matrix:
    row = ''.join(str(_).ljust(3) for _ in row)
    print(row)