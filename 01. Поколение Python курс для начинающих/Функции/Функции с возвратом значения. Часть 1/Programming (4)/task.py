# объявление функции
def find_all(target, symbol):
    # my_list = []
    # for i in range(len(target)):
    #     if target[i] == symbol:
    #         my_list.append(i)
    #
    # return my_list

    return [i for i in range(len(target)) if target[i] == symbol]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
