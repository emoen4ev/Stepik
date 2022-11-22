rows_cols = int(input())

matrix = []

for _ in range(rows_cols):
    curr_row = [int(x) for x in input().split()]

    matrix.append(curr_row)

tr = 0

for i in range(rows_cols):
    tr += matrix[i][i]

print(tr)