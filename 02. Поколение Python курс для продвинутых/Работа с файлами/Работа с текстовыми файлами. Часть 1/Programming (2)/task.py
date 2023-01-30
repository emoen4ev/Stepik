from random import randint


file = open('lines.txt', 'rt', encoding='UTF-8')

file_data = file.readlines()

random_row = randint(0, len(file_data) - 1)

print(file_data[random_row])

file.close()