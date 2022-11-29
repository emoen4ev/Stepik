rows_1, cols_1 = [int(_) for _ in input().split()]
matrix_1 = [[int(_) for _ in input().split()] for _ in range(rows_1)]

input()

rows_2, cols_2 = [int(_) for _ in input().split()]
matrix_2 = [[int(_) for _ in input().split()] for _ in range(rows_2)]

matrix_3 = [[0] * cols_2 for _ in range(rows_1)]

for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_1):
            matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]

for row in matrix_3:
    print(*row)