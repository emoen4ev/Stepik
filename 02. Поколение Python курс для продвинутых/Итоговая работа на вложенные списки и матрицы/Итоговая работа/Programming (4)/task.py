n = int(input())

matrix = [input().split() for _ in range(n)]

result = 'YES'

for i in range(n):
    k = n - i - 1

    for j in range(k):
        r = n - j - 1

        if matrix[i][j] != matrix[r][k]:
            result = 'NO'
            break

    if result == 'NO':
        break

print(result)