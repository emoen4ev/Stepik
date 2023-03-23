"""
Количество дней 😎

Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных:
На вход программе подаются год и полное название месяца на английском, разделенные пробелом.

Формат выходных данных:
Программа должна вывести единственное число — количество дней во введенном месяце.
"""

from calendar import monthrange, month_name

initial_data = input().split()

year, month = int(initial_data[0]), initial_data[1]
month_number = list(month_name).index(month)

result = monthrange(year, month_number)[1]

print(result)

'''
Sample Input 1:
1983 January

Sample Output 1:
31

----------------------------------------------------------------

Sample Input 2:
1956 February

Sample Output 2:
29

----------------------------------------------------------------

Sample Input 3:
1959 March

Sample Output 3:
31
'''