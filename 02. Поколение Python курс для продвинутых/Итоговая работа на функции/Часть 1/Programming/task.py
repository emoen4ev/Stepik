def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    data = [
        f'To: {mail}',
        f'Приветствую, {name}!',
        f'Вам назначен экзамен, который пройдет {date}, в {time}.',
        f'По адресу: {place}.',
        f'Экзамен будет проводить {teacher} в кабинете {number}.',
        'Желаем удачи на экзамене!',
    ]

    return '\n'.join(data)


# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))