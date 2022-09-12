# объявление функции
def get_month(language, number):
    result = ''

    month_ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
                'октябрь', 'ноябрь', 'декабрь']
    month_eng = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                 'october', 'november', 'december']

    if language == 'ru':
        result = month_ru[number]
    if language == 'en':
        result = month_eng[number]

    return result


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))