import random


def is_valid(data):
    return data.isdigit() and int(data) in range(1, 101)


x = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')

user_input = input('Введи число от 1 до 100: ' + '\n')

# while not is_valid(user_input):
#     print('А может быть все-таки введем целое число от 1 до 100?')
#
#     user_input = input()
#
# user_input = int(user_input)

while True:
    if not is_valid(user_input):
        print('А может быть все-таки введем целое число от 1 до 100?')
        user_input = input()
        continue
    user_input = int(user_input)
    break