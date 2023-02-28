"""
Во время решения очередной задачи программист фиксирует время начала и окончания ее решения
и добавляет полученные результаты в список data.
Каждый результат представляет собой кортеж,
первым элементом которого является время начала решения в виде строки в формате HH:MM,
вторым элементом — время окончания решения в виде строки в том же формате.
Дополните приведенный ниже код, чтобы он вывел общее целое количество минут,
которое программист затратил на решение всех задач.
"""

from datetime import datetime, timedelta

pattern = '%H:%M'
# time_for_work = 0

data = [
    ('07:14', '08:46'),
    ('09:01', '09:37'),
    ('10:00', '11:43'),
    ('12:13', '13:49'),
    ('15:00', '15:19'),
    ('15:58', '17:24'),
    ('17:57', '19:21'),
    ('19:30', '19:59'),
]

# for el in data:
#     start = datetime.strptime(el[0], pattern)
#     end = datetime.strptime(el[1], pattern)
#     time_for_work += (end - start).seconds

time_for_work = sum([datetime.strptime(el[1], pattern) - datetime.strptime(el[0], pattern)
                     for el in data], start=timedelta()).seconds

time_for_work //= 60

print(time_for_work)