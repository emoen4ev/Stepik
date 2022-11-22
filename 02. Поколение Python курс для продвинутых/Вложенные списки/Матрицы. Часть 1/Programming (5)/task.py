rows_cols = int(input())

matrix = []
current_part = []

for _ in range(rows_cols):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for i in range(rows_cols):
    for j in range(rows_cols):
        k = rows_cols - 1 - j
        if (j <= i <= k) or (k <= i <= j):
            current_part.append(matrix[i][j])

largest = max(current_part)

print(largest)