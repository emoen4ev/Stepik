from random import choices


with open('random.txt', 'w', encoding='utf-8') as output_file:
    random_data = choices(range(111, 778), k=25)
    data_for_writing = '\n'.join(str(el) for el in random_data)
    output_file.writelines(data_for_writing)

    # print(*random_data, sep='\n', file=output_file)

# with open('random.txt', 'rt', encoding='utf-8') as file:
#     data = file.readlines()
# print(data)