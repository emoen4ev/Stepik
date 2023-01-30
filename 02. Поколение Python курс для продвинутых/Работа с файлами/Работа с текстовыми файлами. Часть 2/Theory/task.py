with open('input.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')