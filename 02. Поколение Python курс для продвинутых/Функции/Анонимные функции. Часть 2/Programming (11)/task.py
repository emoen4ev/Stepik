from functools import reduce


def evaluate(coefficients, x):
    n = len(coefficients) - 1
    data = list(map(lambda y: y * (x ** (n - coefficients.index(y))), coefficients))
    result = reduce(lambda a, b: a + b, data)

    print(result)


evaluate(list(map(int, input().split())), int(input()))