with open('words.txt', 'rt', encoding='utf-8') as input_file:
    data = [x.split() for x in input_file][0]

    max_length = len(max(data, key=lambda x: len(x)))

    result = list(filter(lambda x: len(x) == max_length, data))

    print(*result, sep='\n')