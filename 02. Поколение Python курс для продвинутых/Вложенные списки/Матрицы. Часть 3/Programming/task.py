rows, cols = map(int, input().split())

matrix = []

for i in range(rows):
    current_row = []

    if i % 2 == 1:
        flag = False
    else:
        flag = True

    for _ in range(cols):
        if flag:
            current_row.append('.')
        else:
            current_row.append('*')
        flag = not flag

    matrix.append(current_row)

for row in matrix:
    print(*row)