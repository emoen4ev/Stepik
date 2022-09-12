import random


def is_valid(data):
    return data.isdigit() and int(data) in range(1, 101)


x = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')

user_input = input('Введи число от 1 до 100: ' + '\n')