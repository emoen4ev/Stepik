# объявление функции
def draw_triangle():
    number_ch = 1
    num_front = 7

    for _ in range(8):
        print(' ' * num_front + '*' * number_ch)
        number_ch += 2
        num_front -= 1


# основная программа
draw_triangle()  # вызов функции