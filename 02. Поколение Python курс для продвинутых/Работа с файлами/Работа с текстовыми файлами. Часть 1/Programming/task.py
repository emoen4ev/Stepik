file_name = input()

file = open(file_name, 'rt', encoding='UTF-8')

data = file.read()

print(data)

file.close()