list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for el in list1:
    current_maximum = max(el)
    if current_maximum > maximum:
        maximum = current_maximum

print(maximum)