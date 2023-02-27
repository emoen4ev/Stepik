"""
Таймер

Часы показывают время в формате HH:MM:SS.
На этих часах запустили таймер, который прозвенит через n секунд.
Напишите программу, которое определит, какое время будет на часах, когда прозвенит таймер.

Формат входных данных:
На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS.
В следующей строке вводится целое неотрицательное число n — количество секунд, через которое должен прозвенеть таймер.

Формат выходных данных:
Программа должна вывести время в формате HH:MM:SS, которое будет на часах, когда прозвенит таймер.
"""

from datetime import datetime, timedelta, time


initial_time = input()
number_seconds = int(input())

pattern = '%H:%M:%S'

current_time = datetime.strptime(initial_time, pattern)

h = current_time.hour
m = current_time.minute
s = current_time.second + number_seconds

new_time = timedelta(hours=h, minutes=m, seconds=s)

seconds = new_time.seconds
new_h = seconds // 3600
new_m = (seconds // 60) % 60
new_s = seconds - (new_h * 3600 + new_m * 60)

result = time(hour=new_h, minute=new_m, second=new_s).strftime(pattern)

print(result)

# ----------------------------------------------------------------

# from datetime import datetime, timedelta
#
# pattern = '%H:%M:%S'
# dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))
#
# print(dt.strftime(pattern))

'''
Sample Input 1:
09:00:00
90

Sample Output 1:
09:01:30

----------------------------------------------------------------

Sample Input 2:
23:59:59
1

Sample Output 2:
00:00:00

----------------------------------------------------------------

Sample Input 3:
13:34:46
456

Sample Output 3:
13:42:22
'''