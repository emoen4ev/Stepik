"""
Количество дней 😉

Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных:
На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.

Формат выходных данных:
Программа должна вывести единственное число — количество дней во введенном месяце.

Примечание 1.
Январь имеет порядковый номер 1, Февраль — 2, Март — 3, и так далее.
"""

from calendar import monthrange

# from datetime import datetime
#
# pattern = '%Y %m'
#
# initial_data = input()
#
# data = datetime.strptime(initial_data, pattern)
# current_year = data.year
# current_month = data.month
#
# result = monthrange(current_year, current_month)[1]
#
# print(result)

# ----------------------------------------------------------------

initial_data = input().split()

year, month = map(int, initial_data)
result = monthrange(year, month)[1]

print(result)

'''
Sample Input 1:
2008 1

Sample Output 1:
31

----------------------------------------------------------------

Sample Input 2:
1977 2

Sample Output 2:
28

----------------------------------------------------------------

Sample Input 3:
2000 3

Sample Output 3:
31
'''