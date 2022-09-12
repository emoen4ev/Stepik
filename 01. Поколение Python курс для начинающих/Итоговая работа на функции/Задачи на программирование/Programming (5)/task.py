# объявление функции
def is_magic(date):
    day, month, year = (int(x) for x in date.split('.'))
    return day * month == year % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))