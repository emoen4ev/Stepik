from math import sqrt


# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)

    return min(x_1, x_2), max(x_1, x_2)


# считываем данные
param_a, param_b, param_c = int(input()), int(input()), int(input())

# вызываем функцию
result = solve(param_a, param_b, param_c)
print(*result)