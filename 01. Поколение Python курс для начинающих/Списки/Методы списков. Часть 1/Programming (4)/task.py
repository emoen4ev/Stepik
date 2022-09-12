number = int(input())
my_list = [1]

for numbers_to_number in range(2, int(number / 2) + 1):
    if number % numbers_to_number == 0:
        my_list.append(numbers_to_number)
my_list.append(number)

print(my_list)