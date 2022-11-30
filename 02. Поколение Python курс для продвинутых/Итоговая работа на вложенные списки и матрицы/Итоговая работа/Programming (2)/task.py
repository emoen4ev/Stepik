rows_cols = int(input())

matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols)]

result = [[0 for _ in range(rows_cols)] for _ in range(rows_cols)]

for cur_row in range(rows_cols):
    for cur_col in range(rows_cols):
        result[cur_col][cur_row] = matrix[cur_row][cur_col]

for line in result:
    print(*line)