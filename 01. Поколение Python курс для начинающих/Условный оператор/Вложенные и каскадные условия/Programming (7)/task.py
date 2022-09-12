n = int(input())
if n < 0 or n > 36:
    print("ошибка ввода")
elif n == 0:
    print("зеленый")
elif 0 < n <= 10:
    if n % 2 == 1:
        print("красный")
    else:
        print("черный")
elif 11 <= n <= 18:
    if n % 2 == 1:
        print("черный")
    else:
        print("красный")
elif 19 <= n <= 28:
    if n % 2 == 1:
        print("красный")
    else:
        print("черный")
else:
    if n % 2 == 1:
        print("черный")
    else:
        print("красный")