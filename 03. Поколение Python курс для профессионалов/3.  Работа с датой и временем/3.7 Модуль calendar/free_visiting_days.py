"""
ТЧМ

Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий граждан
происходит без взимания платы.
Например, в Эрмитаже это третий четверг месяца.

Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.

Формат входных данных:
На вход программе подается натуральное число, представляющее год.

Формат выходных данных:
Программа должна определить все даты бесплатных дней посещения Эрмитажа во введенном году и вывести их.
Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.
"""

from calendar import monthcalendar
from datetime import date

current_year = int(input())

pattern = '%d.%m.%Y'

result = []

for month in range(1, 13):
    counter = 0
    for week in monthcalendar(current_year, month):
        thursday = week[3]
        if thursday:
            counter += 1
        if counter == 3:
            result.append(date(current_year, month, thursday))
            break

# for day in result:
#     print(day.strftime(pattern))

print(*[day.strftime(pattern) for day in result], sep='\n')

# ----------------------------------------------------------------

# import calendar
# from datetime import datetime
#
# free_days = []
# year = int(input())
#
# for i in range(1, 13):
#     c = calendar.monthcalendar(year, i)
#     first_week = c[0]
#     third_week = c[2]
#     fourth_week = c[3]
#     if first_week[calendar.THURSDAY]:
#         free_day = third_week[calendar.THURSDAY]
#     else:
#         free_day = fourth_week[calendar.THURSDAY]
#     free_days.append(datetime(year, i, free_day))
#
# for day in free_days:
#     print(day.strftime('%d.%m.%Y'))

# ----------------------------------------------------------------

'''
Sample Input 1:
2021

Sample Output 1:
21.01.2021
18.02.2021
18.03.2021
15.04.2021
20.05.2021
17.06.2021
15.07.2021
19.08.2021
16.09.2021
21.10.2021
18.11.2021
16.12.2021

----------------------------------------------------------------

Sample Input 2:
2020

Sample Output 2:
16.01.2020
20.02.2020
19.03.2020
16.04.2020
21.05.2020
18.06.2020
16.07.2020
20.08.2020
17.09.2020
15.10.2020
19.11.2020
17.12.2020
'''