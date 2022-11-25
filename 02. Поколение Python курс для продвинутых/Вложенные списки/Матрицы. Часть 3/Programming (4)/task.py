rows_cols = int(input())


def get_value(row, col):
    if row == col or row == rows_cols - col - 1:
        return 1

    return 0


matrix = [[get_value(j, i) for j in range(rows_cols)] for i in range(rows_cols)]

for line in matrix:
    line = ''.join(str(_).ljust(3) for _ in line)
    print(line)