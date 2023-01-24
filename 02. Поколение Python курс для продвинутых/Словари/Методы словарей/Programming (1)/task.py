dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

dict2_2 = dict2.copy()

result = {}

dict2.update(dict1)

for k, v in dict2.items():
    if k not in dict1:
        result[k] = v
    elif k in dict2_2:
        result[k] = dict2_2[k] + v
    else:
        result[k] = v

# print(result)