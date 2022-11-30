rows_cols = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols)]

result = [[0 for _ in range(rows_cols)] for _ in range(rows_cols)]

for i in range(rows_cols):
    for j in range(rows_cols):
        result[j][i] = matrix[i][j]

for line in result:
    print(*line)