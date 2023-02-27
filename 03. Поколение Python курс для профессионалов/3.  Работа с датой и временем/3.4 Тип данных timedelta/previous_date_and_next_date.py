"""
Предыдущая и следующая даты

Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

Формат входных данных:
На вход программе подается дата в формате DD.MM.YYYY.

Формат выходных данных:
Программа должна вывести предыдущую и следующую даты относительно введенной даты,
каждую на отдельной строке, в формате DD.MM.YYYY.

Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.
"""

from datetime import datetime, timedelta


pattern, diff = '%d.%m.%Y', timedelta(days=1)

initial_data = input()
current_date = datetime.strptime(initial_data, pattern)

previous_date, next_date = (current_date - diff).strftime(pattern), (current_date + diff).strftime(pattern)

print(previous_date, next_date, sep='\n')

'''
Sample Input 1:
04.11.2021

Sample Output 1:
03.11.2021
05.11.2021

----------------------------------------------------------------

Sample Input 2:
30.11.2021

Sample Output 2:
29.11.2021
01.12.2021

----------------------------------------------------------------

Sample Input 3:
01.11.2021

Sample Output 3:
31.10.2021
02.11.2021
'''