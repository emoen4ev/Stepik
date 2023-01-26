from functools import reduce


def evaluate(coefficients, x):
    working_indices = range(len(coefficients) - 1, -1, -1)
    processed = map(lambda element_value, work_index: element_value * x ** work_index, coefficients, working_indices)
    result = reduce(lambda a, b: a + b, processed)

    print(result)


evaluate(list(map(int, input().split())), int(input()))