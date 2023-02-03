number_files = int(input())
files = [input() for _ in range(number_files)]

with open('output.txt', 'at', encoding='utf-8') as output_file:
    for current_file in files:
        with open(current_file, 'rt', encoding='utf-8') as input_file:
            input_data = input_file.read()
            output_file.write(input_data)