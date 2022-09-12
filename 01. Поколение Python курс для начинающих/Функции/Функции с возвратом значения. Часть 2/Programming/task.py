# объявление функции
def is_valid_triangle(side_1, side_2, side_3):
    return side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3) and side_3 < (side_1 + side_2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))