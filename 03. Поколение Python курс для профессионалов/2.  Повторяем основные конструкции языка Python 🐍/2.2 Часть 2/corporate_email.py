"""
---------- task 'corporate_email'/ requirements --------
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
например, timyr-guev@beegeek.bzz.
При таком подходе существует проблема тёзок.
Для решения такой проблемы было решено приписывать справа номер.
Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz,
третий — timyr-guev2@beegeek.bzz, и так далее.
Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников
в заранее подготовленном виде (латиницей с символом - между ними).

Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных:
На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке.
На следующей строке задано целое неотрицательное число m — количество новых сотрудников,
которым нужно раздать корпоративные ящики.
Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных:
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались.
"""

number_current_users = int(input())

data = {}
last_part = '@beegeek.bzz'

for _ in range(number_current_users):
    number, idx = 0, None
    user_data = input().split('@')
    user_name = user_data[0]
    for i in range(-1, -len(user_data) - 1, -1):
        if user_name[i].isdecimal():
            idx = user_name.index(user_name[i])
            continue
        break
    if idx is not None:
        number = user_name[idx:]
        user_name = user_name[:idx]
    data.setdefault(user_name, []).append(int(number))

print(data)

number_new_users = int(input())

for _ in range(number_new_users):
    new_name = input()
    if new_name not in data:
        data.setdefault(new_name, []).append(0)
        print(new_name + last_part)
    else:
        pass

print(data)



'''
------- test inputs -----
Sample Input 1:
6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov

Sample Input 2:
2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev
'''

'''
--------- expected outputs --------
Sample Output 1:
ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz

Sample Output 2:
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
'''