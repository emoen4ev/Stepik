n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

matrix_tr = [[matrix[j][i] for j in range(n)] for i in range(n)]

control = [x for x in range(1, n + 1)]

result = 'YES'

for el in control:
    for i in range(n):
        if el not in matrix[i] or el not in matrix_tr[i]:
            result = 'NO'
            break
    if result == 'NO':
        break

print(result)