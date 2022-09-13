number_of_string = int(input())
my_list = []

for _ in range(number_of_string):
    new_string = input()
    my_list.extend(new_string)

print(my_list)