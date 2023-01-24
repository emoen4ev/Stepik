rows_cols = int(input())

matrix = []

results = [
    ['Верхняя четверть:', 0],
    ['Правая четверть:', 0],
    ['Нижняя четверть:', 0],
    ['Левая четверть:', 0],
]

for _ in range(rows_cols):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for i in range(rows_cols):
    for j in range(rows_cols):
        k = rows_cols - 1 - j

        if i < j and i < k:
            results[0][1] += matrix[i][j]
        elif k < i < j:
            results[1][1] += matrix[i][j]
        elif j < i and k < i:
            results[2][1] += matrix[i][j]
        elif j < i < k:
            results[3][1] += matrix[i][j]

for result in results:
    print(*result)