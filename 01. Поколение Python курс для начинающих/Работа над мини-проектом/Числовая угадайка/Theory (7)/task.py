import random


def is_valid(*args):
    data = args[0]
    lower_limit = 1
    upper_limit = 100

    if len(args) > 1:
        lower_limit = args[1]
        upper_limit = args[2]

    return data.isdigit() and int(data) in range(lower_limit, upper_limit + 1)


def verify_user_data(*args):
    input_data = args[0]
    lower_limit = 1
    upper_limit = 100

    if len(args) > 1:
        lower_limit = args[1]
        upper_limit = args[2]

    while True:
        if not is_valid(input_data, lower_limit, upper_limit):
            print(f'А может быть все-таки введем целое число от {lower_limit} до {upper_limit} ... ?')
            input_data = input()
            continue
        break

    input_data = int(input_data)

    return input_data


def comparing_the_answer(user_data, x):
    if user_data < x:
        return 'Ваше число меньше загаданного, попробуйте еще разок ... '
    elif user_data > x:
        return 'Ваше число больше загаданного, попробуйте еще разок ... '
    else:
        return 'Вы угадали, поздравляем!'


def confirm_new_try(result):
    while result not in ['да', 'нет']:
        print("Придется вводить либо 'да', либо 'нет',... будешь вводить, пока не научишься ... !")
        result = input('Хочешь попробовать еще раз ... ?  (да / нет)' + '\n')
        continue
    return result


def confirm_new_number(result):
    while result not in ['да', 'нет']:
        print("Придется вводить либо 'да', либо 'нет',... будешь вводить, пока не научишься ... !")
        result = input('Хочешь сгенерирую другое число, чтобы угадать ... ?   (да / нет)' + '\n')
        continue
    return result


def start_game():
    rand_counter = 0
    try_counter = 0
    x = 0

    low = input('Введите нижнюю границу диапазона, в пределах от 1 до 100: ' + '\n')

    lower_limit = verify_user_data(low)

    up = input('Введите верхнюю границу диапазона, в пределах от 1 до 100: ' + '\n')

    upper_limit = verify_user_data(up)

    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit

    while True:

        if rand_counter == 0:
            x = random.randint(lower_limit, upper_limit)
            rand_counter += 1
            print(x)

        user_input = input(f'Введи число от {lower_limit} до {upper_limit}: ' + '\n')

        try_counter += 1

        correct_input = verify_user_data(user_input, lower_limit, upper_limit)

        print(comparing_the_answer(correct_input, x))

        new_try = input('Хочешь попробовать еще раз ... ?  (да / нет)' + '\n').lower()

        new_try = confirm_new_try(new_try)

        if new_try == 'нет':
            if correct_input != x:
                print(f'Число, которое вы не угадали, было: {x}.')
            print(f'Ты сделал {try_counter} попыток угадать число.')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся ...')
            break
        else:
            if correct_input == x:
                print(f'Ты угадал число с {try_counter} попыток.')
                rand_counter = 0
                try_counter = 0
            else:
                new_number = input('Хочешь сгенерирую другое число, чтобы угадать ... ?   (да / нет)' + '\n').lower()
                if confirm_new_number(new_number) == 'да':
                    print(f'Ты сделал {try_counter} попыток угадать число.')
                    rand_counter = 0
                    try_counter = 0
            continue


print('Добро пожаловать в числовую угадайку ...')

start_game()