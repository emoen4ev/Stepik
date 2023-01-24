rows, cols = [int(_) for _ in input().split()]

matrix = [[1] * cols for _ in range(rows)]

value = 0

for k in range(rows * cols):
    for cur_row in range(rows):
        for cur_col in range(cols):
            if cur_row + cur_col == k:
                value += 1
                matrix[cur_row][cur_col] = value

for row in matrix:
    row = ''.join(str(_).ljust(3) for _ in row)
    print(row)