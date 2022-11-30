n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    value = i
    for j in range(n):
        if j > i:
            value += 1
            matrix[i][j] = value

        elif j < i:
            matrix[i][j] = value
            value -= 1

for line in matrix:
    print(*line)