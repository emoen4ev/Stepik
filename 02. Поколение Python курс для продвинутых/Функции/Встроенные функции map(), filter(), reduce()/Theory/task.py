def increase(num):
    return num + 7


numbers = [1, 2, 3, 4, 5, 6]
new_numbers = map(increase, numbers)

print(new_numbers)

new_numbers_1 = list(map(increase, numbers))
print(new_numbers_1)

new_numbers_2 = tuple(map(increase, numbers))
print(new_numbers_2)

for num in new_numbers:    #  итерируем циклом for
    print(num)