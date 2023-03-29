"""
Гуру прогрессий

Дана последовательность целых чисел.
Напишите программу, которая определяет, является ли данная последовательность прогрессией,
и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх),
в каждой строке записано натуральное число — очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:

Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
Не прогрессия, если введенная последовательность чисел не является прогрессией

Примечание 1. Гарантируется, что вид прогрессии определяется однозначно.
"""

from sys import stdin

is_arithmetic_progression = True
is_geometric_progression = True
counter = 0
previous_number = next_number = 0
diff = ratio = 0

for line in stdin:
    line = int(line)

    if counter == 0:
        previous_number = line
        counter += 1
        continue
    else:
        next_number = line

    if counter < 2:
        diff = next_number - previous_number
        ratio = next_number / previous_number
        counter = 2

    if next_number - previous_number != diff:
        is_arithmetic_progression = False
    if next_number / previous_number != ratio:
        is_geometric_progression = False

    if not is_arithmetic_progression and not is_geometric_progression:
        print('Не прогрессия')
        break

    previous_number = next_number

if is_geometric_progression:
    print('Геометрическая прогрессия')
elif is_arithmetic_progression:
    print('Арифметическая прогрессия')

'''
Sample Input 1:
1
2
3
4
5

Sample Output 1:
Арифметическая прогрессия

----------------------------------------------------------------

Sample Input 2:
2
4
8
16

Sample Output 2:
Геометрическая прогрессия

----------------------------------------------------------------

Sample Input 3:
1
9
1
1
4
5

Sample Output 3:
Не прогрессия
'''