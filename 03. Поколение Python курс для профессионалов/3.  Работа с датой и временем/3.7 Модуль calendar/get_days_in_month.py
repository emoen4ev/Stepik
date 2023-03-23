"""
Функция get_days_in_month()

Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
year — натуральное число
month — полное название месяца на английском

Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:
get_days_in_month(2021, 'December')
должен вернуть список:
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_days_in_month(),
но не код, вызывающий ее.
"""

from calendar import monthrange, month_name
from datetime import datetime


def get_days_in_month(year: int, month: str) -> list:
    result = []
    month_number = list(month_name).index(month)
    number_days = monthrange(year, month_number)[1]

    for day in range(1, number_days + 1):
        current_date = datetime(year, month_number, day).date()
        result.append(current_date)

    return result

# print(get_days_in_month(1982, 'January'))
# print(get_days_in_month(2005, 'February'))