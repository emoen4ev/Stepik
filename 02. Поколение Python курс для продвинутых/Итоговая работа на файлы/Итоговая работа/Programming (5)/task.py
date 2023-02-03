# file_name = input()
# # file_name = 'test_file.txt'
#
# with open('forbidden_words_1.txt', 'rt', encoding='utf-8') as input_file:
#     forbidden_words = [word.strip().split() for word in input_file][0]
#
# with open(file_name, 'rt', encoding='utf-8') as working_file:
#     for line in working_file:
#         new_line = line.split()
#         for idx, word in enumerate(new_line):
#             for forbidden_word in forbidden_words:
#                 if forbidden_word in word.lower():
#                     new_part = '*' * len(forbidden_word)
#                     new_word = word.lower().replace(forbidden_word, new_part)
#                     new_line[idx] = new_word
#
#         result = ' '.join(new_line)
#         print(result)

# # ------------------------------------

# file_name = input()
file_name = 'test_file.txt'

with open('forbidden_words_1.txt', 'rt', encoding='utf-8') as input_file:
    forbidden_words = [word.strip().split() for word in input_file][0]

with open(file_name, 'rt', encoding='utf-8') as working_file:
    for line in working_file:
        print(line.strip())
        for forbidden_word in forbidden_words:
            if forbidden_word in line.lower().strip():
                new_part = '*' * len(forbidden_word)
                new_line = line.replace(forbidden_word, new_part)
            line = new_line


        print(line)