"""
Количество секунд

Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.

Формат входных данных:
На вход программе подается время в формате HH:MM:SS.

Формат выходных данных:
Программа должна вывести целое количество секунд, прошедшее с начала суток.

Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.
"""

from datetime import datetime, timedelta


pattern = '%H:%M:%S'

initial_data = input()
current_time = datetime.strptime(initial_data, pattern)

h = current_time.hour
m = current_time.minute
s = current_time.second

result = timedelta(hours=h, minutes=m, seconds=s).seconds

print(result)

# ----------------------------------------------------------------

# start = datetime.strptime('00:00:00', pattern)
# input_time = datetime.strptime(initial_data, pattern)
# delta = input_time - start
#
# print(delta.seconds)

'''
Sample Input 1:
00:01:01

Sample Output 1:
61

----------------------------------------------------------------

Sample Input 2:
00:00:00

Sample Output 2:
0

----------------------------------------------------------------

Sample Input 3:
12:12:12

Sample Output 3:
43932
'''