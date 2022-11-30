rows_cols = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols)]

largest = matrix[rows_cols - 1][rows_cols - 1]

for cur_row in range(rows_cols):
    k = rows_cols - cur_row - 2

    for cur_col in range(rows_cols - 1, k, -1):
        if matrix[cur_row][cur_col] > largest:
            largest = matrix[cur_row][cur_col]

print(largest)