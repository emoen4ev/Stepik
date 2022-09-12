# объявление функции
def merge(list_1, list_2):
    my_result = []

    index_list_1 = 0
    index_list_2 = 0

    while index_list_1 < len(list_1) and index_list_2 < len(list_2):
        if list_1[index_list_1] <= list_2[index_list_2]:
            my_result.append(list_1[index_list_1])
            index_list_1 += 1
        else:
            my_result.append(list_2[index_list_2])
            index_list_2 += 1

    if index_list_1 < len(list_1):
        my_result += list_1[index_list_1:]
    if index_list_2 < len(list_2):
        my_result += list_2[index_list_2:]

    return my_result


# считываем данные
numbers_1 = [int(c) for c in input().split()]
numbers_2 = [int(c) for c in input().split()]


# вызываем функцию
print(merge(numbers_1, numbers_2))