how_many_strings = int(input())
my_first_list = []

for number in range(how_many_strings):
    string = input()
    my_first_list.append(string)

number_of_letter = int(input())

for index_of_my_first_list in range(len(my_first_list)):
    element = my_first_list[index_of_my_first_list]
    if len(element) < number_of_letter:
        continue
    else:
        numbered_letter_of_element = element[number_of_letter - 1]
        print(numbered_letter_of_element, end="")