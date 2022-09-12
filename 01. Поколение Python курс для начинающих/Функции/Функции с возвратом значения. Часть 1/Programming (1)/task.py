# объявление функции
def get_days(month):
    if month == 2:
        return 28
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
