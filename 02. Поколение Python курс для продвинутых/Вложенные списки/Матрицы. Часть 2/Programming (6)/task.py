rows_cols = int(input())

matrix = [input().split() for _ in range(rows_cols)]

k = rows_cols // 2

for i in range(k):
    for j in range(rows_cols):
        m = rows_cols - i - 1
        matrix[i][j], matrix[m][j] = matrix[m][j], matrix[i][j]

for i in range(rows_cols - 1):
    for j in range(i + 1, rows_cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)