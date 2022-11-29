rows_cols = int(input())

initial_matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols)]

power = int(input())

current_powered_matrix = initial_matrix

result = []

for _ in range(power - 1):
    result = [[0] * rows_cols for _ in range(rows_cols)]

    for i in range(rows_cols):
        for j in range(rows_cols):
            for k in range(rows_cols):
                result[i][j] += initial_matrix[i][k] * current_powered_matrix[k][j]

    current_powered_matrix = result

for row in result:
    print(*row)