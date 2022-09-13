number_of_numbers = int(input())

negative_numbers = []
zeros = []
positive_numbers = []

for number in range(number_of_numbers):
    new_number = int(input())
    if new_number < 0:
        negative_numbers.append(new_number)
    elif new_number == 0:
        zeros.append(new_number)
    else:
        positive_numbers.append(new_number)

print(*(negative_numbers + zeros + positive_numbers), sep='\n')

