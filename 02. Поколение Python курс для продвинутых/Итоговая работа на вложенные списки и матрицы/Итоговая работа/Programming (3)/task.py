n = int(input())

matrix = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        k = n - i - 1

        if i == n // 2 or j == n // 2:
            matrix[i][j] = '*'
        elif i == j:
            matrix[i][j] = '*'
        elif j == k:
            matrix[i][j] = '*'

for line in matrix:
    print(*line)