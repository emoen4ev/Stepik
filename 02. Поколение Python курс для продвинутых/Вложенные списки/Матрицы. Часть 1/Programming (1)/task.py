rows, cols = int(input()), int(input())

matrix = []

for _ in range(rows):
    current_row = [input() for _ in range(cols)]

    matrix.append(current_row)

for row in matrix:
    print(*row)

print()

for col in range(cols):
    for row in matrix:
        print(row[col], end=' ')
    print()