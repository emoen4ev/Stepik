"""
Високосный год

Напишите программу, которая определяет, является ли год високосным.

Формат входных данных:
На вход программе в первой строке подается целое число n,
в последующих n строках вводятся натуральные числа, представляющие года.

Формат выходных данных:
Программа должна для каждого введенного года вывести True, если он является високосным, или False в противном случае.
"""

import calendar

number_years = int(input())

for _ in range(number_years):
    print(calendar.isleap(int(input())))

'''
Sample Input 1:
1
2021

Sample Output 1:
False

----------------------------------------------------------------

Sample Input 2:
4
1999
2000
2001
2002

Sample Output 2:
False
True
False
False

----------------------------------------------------------------

Sample Input 3:
3
4433
2048
9757

Sample Output 3:
False
True
False
'''