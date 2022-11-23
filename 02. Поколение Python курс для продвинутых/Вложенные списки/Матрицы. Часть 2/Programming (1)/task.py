rows, cols = int(input()), int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

result_row, result_col = 0, 0

for current_row in range(rows):
    for current_col in range(cols):
        if matrix[current_row][current_col] > matrix[result_row][result_col]:
            result_row, result_col = current_row, current_col

print(result_row, result_col)