def sum_of_numbers_in_file(file_name):
    with open(file_name, 'rt', encoding='utf-8') as file:
        data = file.read()
        numbers = []
        number = ''
        for char in data:
            if char.isdigit():
                number += char
            elif number:
                numbers.append(int(number))
                number = ''
        if number:
            numbers.append(int(number))
        return sum(numbers)


filename = "nums.txt"
result = sum_of_numbers_in_file(filename)
print(result)

'''
 123   jhjk
bhjip456qwerty
1x2y3 4 5 6
sfsd 0 dfgfd
10abc20de30pop5 5 5 5
'''

'''
680
'''