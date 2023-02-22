"""
Отсортированные даты

Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.

Формат входных данных:
На вход программе подается натуральное число n, а затем n корректных дат в ISO формате (YYYY-MM-DD),
каждая на отдельной строке.

Формат выходных данных:
Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY.

Примечание 1.
Последовательность называется неубывающей, если каждый ее следующий член не меньше предыдущего, например:
1,1,2,3,4,4,4,5,6,...

Обратите внимание, что такая последовательность не является возрастающей.

Примечание 2.
Считайте, что при форматировании даты с помощью %Y год выводится без ведущих нулей,
так как на серверах Stepik установлен Linux.
"""

from datetime import date


number_dates = int(input())

data_dates = [date.fromisoformat(input()) for _ in range(number_dates)]

for date in sorted(data_dates):
    print(date.strftime('%d/%m/%Y'))

'''
Sample Input 1:
5
2021-08-01
2021-08-02
2021-07-01
2021-06-01
2021-05-01

Sample Output 1:
01/05/2021
01/06/2021
01/07/2021
01/08/2021
02/08/2021

----------------------------------------------------------------

Sample Input 2:
3
2021-11-01
2021-11-01
2021-11-01

Sample Output 2:
01/11/2021
01/11/2021
01/11/2021
'''