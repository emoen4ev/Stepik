rows_cols = int(input())

matrix = []
max_numbers = []

for _ in range(rows_cols):
    current_row = [int(x) for x in input().split()]

    matrix.append(current_row)

for i in range(rows_cols):
    current_part = [matrix[i][j] for j in range(i + 1)]
    current_max = max(current_part)
    max_numbers.append(current_max)

max_numbers = max(max_numbers)

print(max_numbers)