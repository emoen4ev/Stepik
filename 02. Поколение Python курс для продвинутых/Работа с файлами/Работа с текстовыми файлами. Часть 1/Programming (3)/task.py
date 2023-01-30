file = open('numbers.txt', 'rt', encoding='utf-8')

result = 0

for line in file:
    result += int(line)

print(result)

file.close()