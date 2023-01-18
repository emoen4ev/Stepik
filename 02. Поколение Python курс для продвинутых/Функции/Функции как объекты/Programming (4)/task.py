from math import sin


def get_calculated(operation):
    def get_current_value():
        return data_map[operation]

    return get_current_value()


number = int(input())
command = input()

data_map = {'квадрат': number ** 2,
            'куб': number ** 3,
            'корень': number ** (1 / 2),
            'модуль': abs(number),
            'синус': sin(number),
            }

print(get_calculated(command))