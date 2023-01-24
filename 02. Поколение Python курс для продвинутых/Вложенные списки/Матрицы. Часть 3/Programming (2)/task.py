# rows, cols = [int(x) for x in input().split()]
rows, cols = map(int, input().split())

matrix = []
value = 0

for _ in range(rows):
    current_row = []
    for _ in range(cols):
        value += 1
        current_row.append(value)

    matrix.append(current_row)

for row in matrix:
    print(''.join(str(x).ljust(3) for x in row))