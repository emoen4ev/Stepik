rows_cols = int(input())

tr = 0

# matrix = []
#
# for _ in range(rows_cols):
#     curr_row = [int(x) for x in input().split()]
#
#     matrix.append(curr_row)
#
# for i in range(rows_cols):
#     tr += matrix[i][i]

for i in range(rows_cols):
    tr += int(input().split()[i])

print(tr)