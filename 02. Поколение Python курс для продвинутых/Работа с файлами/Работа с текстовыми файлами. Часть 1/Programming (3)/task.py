file = open('numbers.txt', 'rt', encoding='utf-8')

result = 0

for line in file:
    result += int(line)

# result_1 = sum(map(int, file))

print(result)
# print(result_1)

file.close()