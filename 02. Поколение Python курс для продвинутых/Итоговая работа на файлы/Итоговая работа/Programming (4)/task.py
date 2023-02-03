file_name = input()

with open(file_name, 'rt', encoding='utf-8') as input_file:
    data = [line.strip('\n') for line in input_file]

    result = data[len(data) - 10:] if len(data) > 9 else data

    print(*result, sep='\n')