from random import uniform

n = 10 ** 6  # количество испытаний

x_0 = 2
y_0 = 2
s_0 = x_0 * y_0

k = 0

for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if x ** 2 + y ** 2 - 1 <= 0:
        k += 1

s = (k / n) * s_0

print(s)