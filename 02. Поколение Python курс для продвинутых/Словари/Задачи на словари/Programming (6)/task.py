word = input()
n = int(input())

chars_data = {}
word_data = {}
result = {}

for _ in range(n):
    ch, number = input().split(': ')
    chars_data.setdefault(ch, int(number))

chars_data_sorted = sorted(chars_data.items(), key=lambda x: x[1])

for symbol in word:
    if symbol in word_data:
        continue
    word_data.setdefault(symbol, word.count(symbol))

word_data_sorted = sorted(word_data.items(), key=lambda x: x[1])

for i in range(len(chars_data_sorted)):
    k = word_data_sorted[i][0]
    v = chars_data_sorted[i][0]
    result.setdefault(k, v)

for el in word:
    print(result[el], end='')