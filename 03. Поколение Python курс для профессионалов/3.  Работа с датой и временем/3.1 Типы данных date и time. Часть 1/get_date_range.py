"""
Функция get_date_range()

Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
start — начальная дата, тип date
end — конечная дата, тип date

Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно.
Если start > end, функция должна вернуть пустой список.
"""

from datetime import date


def get_date_range(start: date, end: date) -> list[date]:
    my_list = list(range(start.toordinal(), end.toordinal() + 1))

    return [date.fromordinal(x) for x in my_list]


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 3)

print(get_date_range(date1, date2))

'''
Sample Input 1:

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')

Sample Output 1:

2021-10-01
2021-10-02
2021-10-03
2021-10-04
2021-10-05

Sample Input 2:

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))

Sample Output 2:

[datetime.date(2019, 6, 5)]
'''