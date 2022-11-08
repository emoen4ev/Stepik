counters = [0, 0, 0, 0]
names = [
    'Первая четверть:',
    'Вторая четверть:',
    'Третья четверть:',
    'Четвертая четверть:'
]

number_points = int(input())

while number_points:
    x, y = map(int, input().split())

    if x > 0:
        if y > 0:
            counters[0] += 1
        elif y < 0:
            counters[3] += 1

    elif x < 0:
        if y > 0:
            counters[1] += 1
        elif y < 0:
            counters[2] += 1

    number_points -= 1

for i in range(4):
    print(names[i], counters[i])