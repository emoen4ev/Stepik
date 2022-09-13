number_of_strings = int(input())
initial_list = []
key_list = []

for number in range(number_of_strings):
    new_string = input()
    initial_list.append(new_string)

keyword = input()

for string in initial_list:
    if keyword.lower() in string.lower():
        key_list.append(string)

print(*key_list, sep='\n')
