"""
FAKE NEWS

Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
Напишите программу, которая принимает на вход текущие дату и время и определяет,
сколько времени осталось до выхода курса.

Формат входных данных:
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных:
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:
До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов

Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:
До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут

Если в данном случае количество минут равно нулю, то вывести нужно только часы.
Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:
Курс уже вышел!

Примечание 1.
Программа должна подбирать правильную форму для существительных «день» и «минута».

Для этого можете смело взять свою функцию choose_plural() из этой задачи:
03. Поколение Python курс для профессионалов/2. Повторяем основные конструкции языка Python 🐍/2.1 Часть 1/choose_plural.py
"""

from datetime import datetime


def choose_plural(amount: int, declensions: tuple) -> str:
    cases = (2, 0, 1, 1, 1, 2)
    index = (4 < amount % 100 < 20) and 2 or cases[min(amount % 10, 5)]

    return f'{amount} {declensions[index]}'


pattern = '%d.%m.%Y %H:%M'

initial_start_date = '08.11.2022 12:00'
start_date = datetime.strptime(initial_start_date, pattern)

initial_current_date = input()
current_date = datetime.strptime(initial_current_date, pattern)

if current_date < start_date:
    remaining_time = start_date - current_date

    remaining_days = remaining_time.days
    remaining_hours = remaining_time.seconds // 3600
    remaining_minutes = remaining_time.seconds % 3600 // 60

    plural_dict = {
        'd': ('день', 'дня', 'дней'),
        'h': ('час', 'часа', 'часов'),
        'm': ('минута', 'минуты', 'минут'),
    }

    first_part = 'До выхода курса осталось:'
    second_part = (remaining_days > 0 and remaining_hours > 0
                   and f'{choose_plural(remaining_days, plural_dict["d"])} и'
                       f' {choose_plural(remaining_hours, plural_dict["h"])}') \
                  or (remaining_days > 0 and f'{choose_plural(remaining_days, plural_dict["d"])}') \
                  or (remaining_hours > 0 and remaining_minutes > 0
                      and f'{choose_plural(remaining_hours, plural_dict["h"])} '
                          f'и {choose_plural(remaining_minutes, plural_dict["m"])}') \
                  or (remaining_hours > 0 and f'{choose_plural(remaining_hours, plural_dict["h"])}') \
                  or (1 and f'{choose_plural(remaining_minutes, plural_dict["m"])}')

    print(first_part, second_part)
else:
    print('Курс уже вышел!')

'''
Sample Input 1:
16.11.2021 06:30

Sample Output 1:
До выхода курса осталось: 357 дней и 5 часов

----------------------------------------------------------------

Sample Input 2:
6.11.2022 12:00

Sample Output 2:
До выхода курса осталось: 2 дня

----------------------------------------------------------------

Sample Input 3:
08.11.2022 10:30

Sample Output 3:
До выхода курса осталось: 1 час и 30 минут

----------------------------------------------------------------

Sample Input 4:
08.11.2022 09:00

Sample Output 4:
До выхода курса осталось: 3 часа

----------------------------------------------------------------

Sample Input 5:
08.11.2022 11:40

Sample Output 5:
До выхода курса осталось: 20 минут

----------------------------------------------------------------

Sample Input 6:
08.11.2022 12:15

Sample Output 6:
Курс уже вышел!

----------------------------------------------------------------

Sample Input 7:
14.05.2000 18:43

Sample Output 7:
До выхода курса осталось: 8212 дней и 17 часов
'''