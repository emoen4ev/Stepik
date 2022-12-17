from string import punctuation

text = input().split()

result = {}

for word in text:
    word = word.lower().strip(punctuation)

    result[word] = result.get(word, 0) + 1

result = sorted(result.items(), key=lambda x: (x[1], x[0]))

print(result[0][0])