word = input()

data_dict = {
    1: ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'),
    2: ('D', 'G'),
    3: ('B', 'C', 'M', 'P'),
    4: ('F', 'H', 'V', 'W', 'Y'),
    5: ('K'),
    8: ('J', 'X'),
    10: ('Q', 'Z'),
}

result = 0

for symbol in word:
    for k, v in data_dict.items():
        if symbol in v:
            result += k

print(result)