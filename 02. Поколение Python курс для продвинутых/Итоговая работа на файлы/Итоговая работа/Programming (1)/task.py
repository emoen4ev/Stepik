with open('ledger.txt', 'rt', encoding='utf-8') as input_file:
    data = [int(x.strip('$\n')) for x in input_file.readlines()]

    result = f'${sum(data)}'

    print(result)