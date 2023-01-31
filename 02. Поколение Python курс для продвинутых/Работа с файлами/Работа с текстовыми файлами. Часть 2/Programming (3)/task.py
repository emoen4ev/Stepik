with open('numbers.txt', 'rt', encoding='utf-8') as file:
    data = [map(int, current_line.split()) for current_line in file.readlines()]

for current_line in data:
    print(sum(current_line))

'''  --- numbers.txt: ---
  67 89         100
78
  90 7 8 9
 1 2 3 4   5
    90 0       999
'''

'''
256
78
114
15
1089
'''