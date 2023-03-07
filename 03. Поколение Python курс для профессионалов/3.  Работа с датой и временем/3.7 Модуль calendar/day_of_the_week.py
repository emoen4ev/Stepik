"""
День недели

Напишите программу, которая определяет день недели, соответствующий заданной дате.

Формат входных данных:
На вход программе подается дата в формате YYYY-MM-DD.

Формат выходных данных:
Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.
"""

from calendar import day_name
from datetime import datetime

pattern = '%Y-%m-%d'

initial_data = input()

data = datetime.strptime(initial_data, pattern)
day_number = data.weekday()
day_name = day_name[day_number]

print(day_name)

'''
Sample Input 1:
2021-12-10

Sample Output 1:
Friday

----------------------------------------------------------------

Sample Input 2:
2022-01-03

Sample Output 2:
Monday

----------------------------------------------------------------

Sample Input 3:
2021-11-02

Sample Output 3:
Tuesday
'''