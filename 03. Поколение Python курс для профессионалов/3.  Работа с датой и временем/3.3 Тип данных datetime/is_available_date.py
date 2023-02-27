"""
Функция is_available_date() 🌶️

Во время визита очередного гостя сотрудникам отеля приходится проверять,
доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
 - booked_dates — список строковых дат, недоступных для бронирования.
   Элементом списка является либо одиночная дата, либо период (две даты через дефис).
   Например: ['04.11.2021', '05.11.2021-09.11.2021']

 - date_for_booking — одиночная строковая дата или период (две даты через дефис),
   на которую гость желает забронировать номер.
   Например: '01.11.2021' или '01.11.2021-04.11.2021'

Функция is_available_date() должна возвращать True, если дата или период date_for_booking
полностью доступна для бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.
"""

from datetime import datetime


def get_dates_sequence(data: list or str) -> set:
    available_dates = set()
    data = {data} if isinstance(data, str) else data
    for el in data:
        el = el.split('-') if '-' in el else [el]
        if len(el) == 1:
            available_dates.add(datetime.strptime(el[0], '%d.%m.%Y').toordinal())
        else:
            start_date, end_date = datetime.strptime(el[0], '%d.%m.%Y'), datetime.strptime(el[1], '%d.%m.%Y')
            sequence = set(range(start_date.toordinal(), end_date.toordinal() + 1))
            available_dates = available_dates.union({days for days in sequence})
    return available_dates


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    non_available_dates = get_dates_sequence(booked_dates)
    dates_to_book = get_dates_sequence(date_for_booking)

    return True if dates_to_book.isdisjoint(non_available_dates) else False


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

'''
Sample Input 1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

Sample Output 1:
True

----------------------------------------------------------------

Sample Input 2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

Sample Output 2:
False

----------------------------------------------------------------

Sample Input 3:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

Sample Output 3:
False

----------------------------------------------------------------

Sample Input 4:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

Sample Output 4:
False
'''