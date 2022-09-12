# объявление функции
def number_to_words(num):
    result = ''

    list_0_20 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
                 'восемнадцать', 'девятнадцать', 'двадцать']

    list_0_90 = ['ноль', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
                 'восемьдесят', 'девяносто']

    if num in range(0, 21):
        result = list_0_20[num]
    elif num in range(21, 100):
        first_digit = num // 10
        last_digit = num % 10

        if num % 10 == 0:
            result = list_0_90[first_digit]
        else:
            result = list_0_90[first_digit] + ' ' + list_0_20[last_digit]

    return result


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))