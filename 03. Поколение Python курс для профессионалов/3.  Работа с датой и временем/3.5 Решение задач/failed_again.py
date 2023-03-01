"""
Снова не успел

Дан режим работы магазина:

Понедельник	9:00 - 21:00
Вторник	9:00 - 21:00
Среда	9:00 - 21:00
Четверг	9:00 - 21:00
Пятница	9:00 - 21:00
Суббота	10:00 - 18:00
Воскресенье	10:00 - 18:00

Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут,
оставшееся до закрытия магазина.

Формат входных данных:
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных:
Программа должна вывести количество минут, которое осталось до закрытия магазина,
или текст Магазин не работает, если он закрыт.
"""

from datetime import datetime, time

initial_data = input()

working_time = {
    1: (time(hour=9, minute=0), time(hour=21, minute=0)),
    2: (time(hour=9, minute=0), time(hour=21, minute=0)),
    3: (time(hour=9, minute=0), time(hour=21, minute=0)),
    4: (time(hour=9, minute=0), time(hour=21, minute=0)),
    5: (time(hour=9, minute=0), time(hour=21, minute=0)),
    6: (time(hour=10, minute=0), time(hour=18, minute=0)),
    7: (time(hour=10, minute=0), time(hour=18, minute=0)),
}

pattern = '%d.%m.%Y %H:%M'

my_shopping_time = datetime.strptime(initial_data, pattern)
week_day = my_shopping_time.isoweekday()

shop_opened = working_time[week_day][0]
shop_closed = working_time[week_day][1]

if my_shopping_time.time() < shop_opened or shop_closed <= my_shopping_time.time():
    print('Магазин не работает')
else:
    shop_closed = datetime.combine(my_shopping_time.date(), shop_closed)
    remaining_minutes = (shop_closed - my_shopping_time).seconds // 60

    print(remaining_minutes)

'''
Sample Input 1:
01.11.2021 20:45

Sample Output 1:
15

----------------------------------------------------------------

Sample Input 2:
02.11.2021 21:15

Sample Output 2:
Магазин не работает

----------------------------------------------------------------

Sample Input 3:
07.11.2021 10:00

Sample Output 3:
480
'''