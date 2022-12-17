from random import randint

n = int(input())    # количество попыток

for _ in range(n):
    result = randint(1, 6)
    print(result)