from random import randint

length = int(input())  # длина пароля

for _ in range(length):
    x = randint(0, 1)
    ch_lower = chr(randint(97, 122))
    ch_upper = chr(randint(65, 90))
    result = (ch_lower, ch_upper)[x]
    print(result, end='')