import random

n = int(input())    # количество попыток

result = [('Орел', 'Решка')[random.randint(0, 1)] for _ in range(n)]

print(*result, sep='\n')