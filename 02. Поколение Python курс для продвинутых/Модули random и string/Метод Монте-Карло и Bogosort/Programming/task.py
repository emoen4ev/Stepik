from random import uniform

n = 10 ** 6  # количество испытаний

x_0 = 4
y_0 = 4
s_0 = x_0 * y_0

k = 0

for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)

    if 3 * x + y ** 2 - 2 <= 0 <= x ** 3 + y ** 4 + 2:
        k += 1

s = (k / n) * s_0

print(s)