file = open('nums.txt', 'rt', encoding='utf-8')

data = file.read().split()

# print(data)

result = sum(map(int, data))

print(result)

file.close()