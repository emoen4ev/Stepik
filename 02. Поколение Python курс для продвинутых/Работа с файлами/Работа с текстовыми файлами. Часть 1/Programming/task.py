name = input()

file_name = open(name, 'rt', encoding='UTF-8')

data = file_name.read()

print(data)

file_name.close()