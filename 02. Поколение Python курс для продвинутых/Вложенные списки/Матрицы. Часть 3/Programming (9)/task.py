rows, cols = map(int, input().split())

matrix = [[0 for j in range(cols)] for i in range(rows)]

current_value = 1

start_row, start_column = 0, 0

while start_row < rows and start_column < cols:

    for col in range(start_column, cols):
        matrix[start_row][col] = current_value
        current_value += 1
    start_row += 1

    for row in range(start_row, rows):
        matrix[row][cols - 1] = current_value
        current_value += 1
    cols -= 1

    if start_row < rows:
        for col in range(cols - 1, start_column - 1, -1):
            matrix[rows - 1][col] = current_value
            current_value += 1
        rows -= 1

    if start_column < cols:
        for row in range(rows - 1, start_row - 1, -1):
            matrix[row][start_column] = current_value
            current_value += 1
        start_column += 1

for line in matrix:
    line = ''.join(str(_).ljust(3) for _ in line)
    print(line)