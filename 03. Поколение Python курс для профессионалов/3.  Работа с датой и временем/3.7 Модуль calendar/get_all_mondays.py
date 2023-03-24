"""
Функция get_all_mondays()

Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
year — натуральное число

Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.

Примечание 1. Например, вызов:
get_all_mondays(2021)
должен вернуть список:
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
"""

from datetime import datetime, timedelta


def get_all_mondays(year: int) -> list:
    result = []
    start_date = datetime(year=year, month=1, day=1)
    final_date = datetime(year=year + 1, month=1, day=1)
    first_week_day = start_date.isoweekday()
    if first_week_day != 1:
        diff = 8 - first_week_day
        start_date += timedelta(days=diff)
    current_date = start_date

    while current_date < final_date:
        result.append(current_date.date())
        current_date += timedelta(days=7)

    return result

# ----------------------------------------------------------------

# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             monday = week[0]
#             if monday:
#                 mondays.append(date(year, month, monday))
#     return mondays

# ----------------------------------------------------------------

# from calendar import monthcalendar
# from datetime import date
#
# def get_all_mondays(y: int, x=range(1, 13)) -> list:
#     return [date(y, m, i[0]) for m in x for i in monthcalendar(y, m) if i[0]]

# ----------------------------------------------------------------

# import calendar
# from datetime import datetime, date
#
# def get_all_mondays(year):
#     return [date(year, k, i[0]) for k in range(1, 13) for i in calendar.monthcalendar(year, k) if i[0] != 0]

# ----------------------------------------------------------------

# print(get_all_mondays(2021))