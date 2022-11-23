rows_cols = int(input())

matrix = [input().split() for _ in range(rows_cols)]

is_symmetrical = True

for i in range(rows_cols):
    for j in range(rows_cols):
        if matrix[i][j] != matrix[j][i]:
            is_symmetrical = False
            break

    if not is_symmetrical:
        break

print('YES' if is_symmetrical else 'NO')