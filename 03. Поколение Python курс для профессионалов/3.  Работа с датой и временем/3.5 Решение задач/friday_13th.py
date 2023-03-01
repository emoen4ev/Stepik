"""
Пятница, 13-е
Число 13 считалось дьявольским издавна.
Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с Тайной вечерей — где были Христос и 12 апостолов,
один из которых стал предателем. Есть поверье, что для шабаша нужны 12 ведьм и сатана.
В истории число 13 в связке с пятницей стало «несчастливым» в 1307 году,
когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского ордена крестоносцев.
Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 13 апреля.

Докажите, что 13-е число месяца чаще всего приходится на пятницу.
Напишите программу, которая вычисляет,
сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.

Формат входных данных:
На вход программе ничего не подается.

Формат выходных данных:
Программа должна вывести 7 чисел — количество тринадцатых чисел,
которые приходятся на понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье
в период с 01.01.0001 по 31.12.9999.
Числа должны быть расположены каждое на отдельной строке.
"""

from datetime import datetime, timedelta, date
import time

start_time = time.time()

pattern = '%d.%m.%Y'
start_date = '01.01.0001'
end_date = '31.12.9999'
result = {}

start = datetime.strptime(start_date, pattern)
end = datetime.strptime(end_date, pattern)

c = [start + timedelta(days=x) for x in range((end - start).days) if (start + timedelta(days=x)).day == 13]

for x in range((end - start).days):
    current_date = start + timedelta(days=x)
    if current_date.day == 13:
        number = current_date.weekday()
        result.setdefault(number, []).append(current_date)

for k, v in sorted(result.items()):
    print(len(v))

print(f'{time.time() - start_time} seconds')  # 4.9270055294036865 seconds

# ----------------------------------------------------------------

start_time = time.time()

day_13th = [datetime(year=y, month=m, day=13).weekday() for y in range(1, 10000) for m in range(1, 13)]

result = [day_13th.count(week_day) for week_day in range(7)]

print(*result, sep='\n')

print(f'{time.time() - start_time} seconds')  # 0.07400202751159668 seconds
# print("--- %s seconds ---" % (time.time() - start_time))

# ----------------------------------------------------------------

start_time = time.time()

week_days = [0, 0, 0, 0, 0, 0, 0]

for years in range(1, 10000):
    for months in range(1, 13):
        week_days[date(years, months, 13).weekday()] += 1

print(*week_days, sep='\n')

print(f'{time.time() - start_time} seconds')  # 0.03999781608581543 seconds