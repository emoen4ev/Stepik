rows, cols = [int(_) for _ in input().split()]

matrix_1 = [[int(_) for _ in input().split()] for _ in range(rows)]

input()

matrix_2 = [[int(_) for _ in input().split()] for _ in range(rows)]


def get_value(row, col):
    return matrix_1[row][col] + matrix_2[row][col]


matrix_of_sums = [[get_value(i, j) for j in range(cols)] for i in range(rows)]

for line in matrix_of_sums:
    print(*line)