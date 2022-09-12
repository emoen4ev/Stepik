number_of_strings = int(input())

initial_list = []
key_list = []

for number in range(number_of_strings):
    new_string = input()
    initial_list.append(new_string)

number_of_keywords = int(input())

for number in range(number_of_keywords):
    new_key_word = input()
    key_list.append(new_key_word)

for string in initial_list:
    for key in key_list:
        if key.lower() not in string.lower():
            break
    else:
        print(string)
