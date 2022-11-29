rows_cols = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols)]

largest = matrix[rows_cols - 1][rows_cols - 1]

for i in range(rows_cols):
    k = rows_cols - i - 2
    for j in range(rows_cols - 1, k, -1):
        if matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)