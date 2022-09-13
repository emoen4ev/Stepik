numbers_as_string = input()

numbers_as_list = numbers_as_string.split(' ')
numbers_as_numbers = []

for numbers in numbers_as_list:
    numbers = int(numbers)
    numbers_as_numbers.append(numbers)

maximum_value = max(numbers_as_numbers)
minimum_value = min(numbers_as_numbers)

index_max = numbers_as_numbers.index(maximum_value)
index_min = numbers_as_numbers. index(minimum_value)

numbers_as_numbers[index_max], numbers_as_numbers[index_min] = \
    numbers_as_numbers[index_min], numbers_as_numbers[index_max]

print(*numbers_as_numbers)