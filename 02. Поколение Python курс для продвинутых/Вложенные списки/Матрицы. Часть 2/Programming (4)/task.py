rows_cols = int(input())

matrix = [input().split() for _ in range(rows_cols)]

for i in range(rows_cols):
    j = rows_cols - 1 - i
    matrix[i][i], matrix[j][i] = matrix[j][i], matrix[i][i]

for row in matrix:
    print(*row)