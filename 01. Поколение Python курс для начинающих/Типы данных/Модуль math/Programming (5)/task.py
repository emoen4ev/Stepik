import math

a, b, c = float(input()), float(input()), float(input())
d = math.pow(b, 2) - 4 * a * c
if d > 0:
    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    print(min(x_1, x_2), max(x_1, x_2), sep="\n")
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Нет корней")

