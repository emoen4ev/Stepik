forbidden_words_file = 'forbidden_words.txt'
# # forbidden_words_file = 'forbidden_words_1.txt'
#
file_name = input()
# # file_name = 'test_file.txt'
# # file_name = 'data.txt'
# # file_name = 'stepik.txt'
# # file_name = 'beegeek.txt'

with open(forbidden_words_file, 'rt', encoding='utf-8') as input_file:
    forbidden_words = input_file.read().strip().split()

with open(file_name, 'rt', encoding='utf-8') as working_file:
    words = working_file.read()

for forbidden_word in forbidden_words:
    while forbidden_word in words.lower():
        start = words.lower().find(forbidden_word)
        words = words[:start] + '*' * len(forbidden_word) + words[start + len(forbidden_word):]
print(words)