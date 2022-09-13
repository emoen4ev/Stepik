how_many_numbers = int(input())

my_list = []

for number_of_numbers in range(how_many_numbers):
    next_number = int(input())
    my_list.append(next_number)

del my_list[1::2]

print(my_list)