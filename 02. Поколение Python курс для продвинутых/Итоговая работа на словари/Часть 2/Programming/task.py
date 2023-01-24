sequence = {
    'A': 'U',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

data = input()

for el in data:
    print(sequence[el], end='')