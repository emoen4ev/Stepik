numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {el: [i for i in range(1, (el // 2) + 1) if el % i == 0] + [el] for el in numbers}

# print(result)