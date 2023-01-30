with open('data.txt', 'rt', encoding='utf-8') as file:
    for line in file.readlines()[::-1]:
        print(line.strip())

#     data = []
#     for line in file:
#         data.append(line.strip())
#
# print(*data[::-1], sep='\n')


'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''