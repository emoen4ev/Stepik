"""
Это точно Python?

Дана последовательность дат. Напишите программу, которая определяет,
в каком порядке расположены даты в данной последовательности.

Формат входных данных:
На вход программе подается произвольное количество строк (две или более),
в каждой строке записана дата в формате DD.MM.YYYY.

Формат выходных данных:
Программа должны вывести текст:

ASC, если даты в введенной последовательности расположены строго в порядке возрастания
DESC, если даты в введенной последовательности расположены строго в порядке убывания
MIX, если даты в введенной последовательности расположены ни в порядке возрастания, ни в порядке убывания
    Параметры ASC и DESC используются в языке SQL для сортировки по возрастанию и по убыванию соответственно.
"""

from sys import stdin
from datetime import datetime

is_asc = True
is_desc = True
counter = 0
pattern = '%d.%m.%Y'
first_date = current_date = datetime.today()

for line in stdin:
    if counter == 0:
        first_date = datetime.strptime(line.strip(), pattern)
        counter = 1
        continue
    else:
        current_date = datetime.strptime(line.strip(), pattern)

    if first_date < current_date:
        is_desc = False
    elif current_date < first_date:
        is_asc = False
    else:
        is_asc = is_desc = False

    if not is_asc and not is_desc:
        print('MIX')
        break

    first_date = current_date

if is_asc:
    print('ASC')
elif is_desc:
    print('DESC')

'''
Sample Input 1:
14.06.2022
20.06.2022
21.06.2022

Sample Output 1:
ASC

----------------------------------------------------------------

Sample Input 2:
01.09.2022
01.08.2022
01.07.2022
01.06.2022
01.05.2022

Sample Output 2:
DESC

----------------------------------------------------------------

Sample Input 3:
10.10.2021
19.01.1999
09.04.2022
01.01.1978

Sample Output 3:
MIX

----------------------------------------------------------------

Sample Input 4:
14.06.2022
20.06.2022
21.06.2022
17.01.2031
18.11.2031
19.11.2031
23.11.2031
01.01.2033
01.11.2043
05.07.2051
05.07.2051

Sample Output 4:
MIX
'''