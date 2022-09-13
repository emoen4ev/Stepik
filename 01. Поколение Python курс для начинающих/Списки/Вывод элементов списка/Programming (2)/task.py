my_list = []

numbers = int(input())

for num in range(numbers):
    new_number = int(input())
    my_list.append(new_number)

# index_min_number = my_list.index(min(my_list))
# del my_list[index_min_number]
# index_max_number = my_list.index(max(my_list))
# del my_list[index_max_number]
#
# print(*my_list, sep='\n')

min_my_list = min(my_list)
max_my_list = max(my_list)

for num in my_list:
    if max_my_list > num > min_my_list:
        print(num, sep='\n')
