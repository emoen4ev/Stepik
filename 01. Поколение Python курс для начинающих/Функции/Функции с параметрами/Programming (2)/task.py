# объявление функции
def print_digit_sum(num):
    print(sum(int(digit) for digit in str(num)))
    # sum_digits = 0
    # for digit in str(num):
    #     sum_digits += int(digit)
    # print(sum_digits)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
