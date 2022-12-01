def get_coordinates(param_1, param_2, param_3):
    x = -param_2 / (2 * param_1)
    y = (4 * param_1 * param_3 - param_2 ** 2) / (4 * param_1)

    return x, y


a, b, c = int(input()), int(input()), int(input())

print(get_coordinates(a, b, c))