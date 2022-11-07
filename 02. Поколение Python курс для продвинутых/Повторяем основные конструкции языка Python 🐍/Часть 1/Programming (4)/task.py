requested_year = int(input())

initial_year = 2000
repetition_period = 12
initial_info = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья',
                'Крыса', 'Бык', 'Тигр', 'Заяц']

x = (requested_year - initial_year) % repetition_period

print(initial_info[x])