from functools import reduce


# def product_of_odds(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result


def product_of_odds(data):
    filtered_data = filter(lambda x: x % 2 == 1, data)
    result = reduce(lambda x, y: x * y, filtered_data, 1)
    return result


# print(product_of_odds([2, 3, 4, 5, 6, 7, 8, 9]))