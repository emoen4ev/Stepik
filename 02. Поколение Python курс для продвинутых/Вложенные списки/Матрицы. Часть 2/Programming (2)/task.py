rows, cols = int(input()), int(input())

matrix = [input().split() for _ in range(rows)]

col_1, col_2 = map(int, input().split())

for row in range(rows):
    matrix[row][col_1], matrix[row][col_2] = matrix[row][col_2], matrix[row][col_1]

for row in matrix:
    print(*row)