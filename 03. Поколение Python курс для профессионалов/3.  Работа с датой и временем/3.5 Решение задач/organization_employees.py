"""
Сотрудники организации 😄

Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
Напишите программу, которая определяет самого старшего сотрудника из данного списка.

Формат входных данных:
На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации.
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных:
Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом.
Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.

Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.
"""

# from datetime import datetime
#
# pattern = '%d.%m.%Y'
# employees_data = {}
#
# number_employees = int(input())
# initial_data = [input().split() for _ in range(number_employees)]
#
# for el in initial_data:
#     names = ' '.join(el[:2])
#     birth_date = datetime.strptime(el[2], pattern)
#
#     employees_data.setdefault(birth_date, []).append(names)
#
# earliest_birth_date = min(employees_data)
# oldest_employees = employees_data[earliest_birth_date]
#
# first_part = earliest_birth_date.strftime(pattern)
# second_part = (len(oldest_employees) > 1 and len(oldest_employees)) or (1 and oldest_employees[0])
#
# print(first_part, second_part)

# ------------------------

from datetime import datetime

pattern = '%d.%m.%Y'
oldest = datetime.max
last_data = [0, 0]

number_employees = int(input())

for _ in range(number_employees):
    name, birthday = input().rsplit(' ', 1)
    birthday = datetime.strptime(birthday, pattern)

    if birthday < oldest:
        oldest = birthday
        last_data[0], last_data[1] = oldest, [name]
    elif birthday == oldest:
        last_data[1].append(name)

first_part = last_data[0].strftime(pattern)
second_part = (len(last_data[1]) > 1 and len(last_data[1])) or (1 and str(*last_data[1]))

print(first_part, second_part)

'''
Sample Input 1:
3
Иван Петров 01.05.1995
Петр Сергеев 29.04.1995
Сергей Иванов 01.01.1996

Sample Output 1:
29.04.1995 Петр Сергеев

----------------------------------------------------------------

Sample Input 2:
3
Иван Петров 01.05.1995
Петр Сергеев 29.05.1995
Сергей Иванов 01.05.1995

Sample Output 2:
01.05.1995 2
'''