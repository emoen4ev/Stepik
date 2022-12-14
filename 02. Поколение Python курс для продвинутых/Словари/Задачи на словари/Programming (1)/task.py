word_1, word_2 = input(), input()

word_1_dict, word_2_dict = {}, {}

for ch in word_1:
    word_1_dict[ch] = word_1_dict.get(ch, 0) + 1

for ch in word_2:
    word_2_dict[ch] = word_2_dict.get(ch, 0) + 1

print('YES' if word_1_dict == word_2_dict else 'NO')