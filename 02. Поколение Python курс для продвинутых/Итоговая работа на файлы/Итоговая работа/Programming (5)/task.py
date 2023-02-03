# file_name = input()
file_name = 'test_file.txt'

with open('forbidden_words_1.txt', 'rt', encoding='utf-8') as input_file:
    forbidden_words = [word.strip().split() for word in input_file][0]

    print(forbidden_words)

with open(file_name, 'rt', encoding='utf-8') as working_file:
    for line in working_file:
        for word in forbidden_words:
            if word in line.lower():
                new_line = line.lower().replace(word, '*' * len(word))
            print(new_line.strip())