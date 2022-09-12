number_of_numbers_entered = int(input())
my_list = []

for current_number_entered in range(number_of_numbers_entered):
    current_number = int(input())
    cube_of_a_current_number = current_number ** 3
    my_list.append(cube_of_a_current_number)

print(my_list)