# объявление функции
def convert_to_miles(km):
    return round(km * 0.6214, 4)


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
