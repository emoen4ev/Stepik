text = input()

key_map = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' ',
}

for symbol in text:
    for key, value in key_map.items():
        symbol = symbol.upper()
        if symbol in value:
            rp = value.index(symbol) + 1
            print(key * rp, end='')
            break