numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.insert(4, 4)
num_add = [5, 6]
numbers.extend(num_add)
del numbers[0]
numbers_copy = numbers.copy()
numbers.extend(numbers_copy)
numbers.insert(3, 25)
print(numbers)