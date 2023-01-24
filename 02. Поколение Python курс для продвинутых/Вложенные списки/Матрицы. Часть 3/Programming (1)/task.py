rows_cols = int(input())

matrix = [[1] * rows_cols for _ in range(rows_cols)]

for row in range(rows_cols):
    k = rows_cols - row - 1
    for col in range(rows_cols):
        if col < k:
            matrix[row][col] = 0
        elif col > k:
            matrix[row][col] = 2

for row in matrix:
    print(*row)