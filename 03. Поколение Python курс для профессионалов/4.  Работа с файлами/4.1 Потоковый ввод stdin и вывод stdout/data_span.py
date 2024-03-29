"""
Размах данных

Дана последовательность дат.
Напишите программу, которая выводит количество дней между максимальной и минимальной датами данной последовательности.

Формат входных данных:
На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных:
Программа должна вывести единственное число —
количество дней между максимальной и минимальной датами введенной последовательности.
"""

from sys import stdin
from datetime import date

data = [date.fromisoformat(line.strip()) for line in stdin]

min_date, max_date = min(data), max(data)

result = (max_date - min_date).days

print(result)

'''
Sample Input 1:
2022-06-15
2022-06-12
2022-06-16
2022-06-30

Sample Output 1:
18

----------------------------------------------------------------

Sample Input 2:
2077-01-01
2077-01-01
2077-01-01

Sample Output 2:
0
'''