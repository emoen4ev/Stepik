m, n = int(input()), int(input())

list_1 = [input() for _ in range(m + n)]

set_1 = set(list_1)

x = len(list_1) - len(set_1)

result = len(set_1) - x

print(result if result else 'NO')