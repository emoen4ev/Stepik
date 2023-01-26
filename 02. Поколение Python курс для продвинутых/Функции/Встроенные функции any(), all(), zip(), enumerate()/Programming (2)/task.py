abscissas, ordinates, applicates = [map(float, input().split()) for _ in range(3)]

r = 2

data = zip(abscissas, ordinates, applicates)

result = all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= r ** 2, data))

print(result)