number_of_strings = int(input())
first_string = input()
my_list = [first_string]

for num in range(number_of_strings - 1):
    new_string = input()
    exists = False
    for strings in my_list:
        if new_string == strings:
            exists = True
            break
    if not exists:
        my_list.append(new_string)

print(*my_list, sep='\n')
