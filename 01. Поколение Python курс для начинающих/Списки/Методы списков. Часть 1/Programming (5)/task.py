how_many_numbers = int(input())
my_list = []
first_number = int(input())

for number in range(how_many_numbers - 1):
    second_number = int(input())
    sum_with_the_next_number = first_number + second_number
    my_list.append(sum_with_the_next_number)
    first_number = second_number

print(my_list)