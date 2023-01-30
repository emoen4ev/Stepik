file_name = input()

file = open(file_name, 'rt', encoding='UTF-8')

data = file.readlines()

print(data[-2])

file.close()