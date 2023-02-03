file_name = input()

with open(file_name, 'rt', encoding='utf-8') as input_file:
    data = input_file.readlines()

    result = len(data)

    print(result)