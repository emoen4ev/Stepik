"""
Календарь на месяц

Напишите программу, которая выводит календарь на заданные год и месяц.

Формат входных данных:
На вход программе подаются год и сокращенное название месяца на английском, разделенные пробелом.

Формат выходных данных:
Программа должна вывести календарь на введенные год и месяц.
"""

from calendar import prmonth
from datetime import datetime

initial_data = input()

pattern = '%Y %b'

data = datetime.strptime(initial_data, pattern)

current_year, current_month = data.year, data.month

prmonth(current_year, current_month)

'''
Sample Input:
2021 Dec

Sample Output:
   December 2021
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
'''