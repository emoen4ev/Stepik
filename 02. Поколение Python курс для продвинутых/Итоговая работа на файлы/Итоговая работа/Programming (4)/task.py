# file_name = input()
#
# with open(file_name, 'rt', encoding='utf-8') as input_file:
#     data = [line.strip('\n') for line in input_file]
#
#     result = data[len(data) - 10:] if len(data) > 9 else data
#
#     print(*result, sep='\n')

# --------------- Примечание 4. Подумайте над ситуацией, когда файл очень большой
# и нерационально считывать все его содержимое в память компьютера. -----------------------

file_name = input()

counter = 0

with open(file_name, 'rt', encoding='utf-8') as input_file:
    for line in input_file:
        counter += 1

    input_file.seek(0)

    if counter < 11:
        for line in input_file:
            print(line.strip())
    else:
        number_line_to_skip = counter - 10

        for line in input_file:
            if number_line_to_skip > 0:
                number_line_to_skip -= 1
                continue
            else:
                print(line.strip())