list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for el in list1:
    total += sum(el)
    counter += len(el)

result = total / counter

print(result)