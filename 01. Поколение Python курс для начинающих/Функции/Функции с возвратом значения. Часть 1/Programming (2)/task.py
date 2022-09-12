# объявление функции
def get_factors(num):
    # list_1 = []
    # for i in range(1, int((num / 2) + 1)):
    #     if num % i == 0:
    #         list_1.append(i)
    # list_1.append(num)
    # return list_1
    return [i for i in range(1, int((num / 2) + 1)) if num % i == 0] + [num]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
