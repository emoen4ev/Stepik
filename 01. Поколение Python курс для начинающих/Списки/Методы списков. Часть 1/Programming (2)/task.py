a_code = ord('a')
z_code = ord('z')
my_list = []
counter = 1

for characters in range(a_code, z_code + 1):
    letter = chr(characters)
    current_characters = letter * counter
    my_list.append(current_characters)
    counter += 1

print(my_list)