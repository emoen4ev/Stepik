rows, cols = [int(x) for x in input().split()]


def get_value(row, col):
    row %= cols
    if row == 0:
        row = cols
    value = row + col
    if value > cols:
        value %= cols
        if value == 0:
            value = cols
    return value


matrix = [[get_value(i, j) for j in range(cols)] for i in range(1, rows + 1)]

for line in matrix:
    line = ''.join(str(_).ljust(3) for _ in line)
    print(line)