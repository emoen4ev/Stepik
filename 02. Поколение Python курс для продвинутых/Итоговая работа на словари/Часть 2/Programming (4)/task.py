def merge(values):  # values - это список словарей
    result = {}
    for el in values:
        for item in el:
            result.setdefault(item, set()).add(el[item])
    return result


# my_list = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
#
# print(merge(my_list))