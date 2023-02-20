"""
---------- task 'files_in_a_file'/ requirements --------
Вам доступен текстовый файл files.txt, содержащий информацию о файлах.
Каждая строка файла содержит три значения, разделенные символом пробела —
имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...

Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы,
и выводит полученные группы файлов, указывая для каждой ее общий объем.
Группы должны быть расположены в лексикографическом порядке названий расширений,
файлы в группах — в лексикографическом порядке их имен.


Примечание 1.
Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB

где Summary — общий объем файлов группы.

Примечание 2.
Гарантируется, что все имена файлов содержат расширение.

Примечание 3.
Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с округлением до целых.
Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах,
а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения.
Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB

Примечание 4.
Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB

Примечание 5.
Указанный файл (files.txt) доступен по ссылке. Ответ на задачу (clue.txt) доступен по ссылке.

Примечание 6.
При открытии файла используйте явное указание кодировки UTF-8.
"""


def get_size_in_bytes(value: int, dimension: str) -> float:
    if dimension in CONVERTING_TABLE:
        return value * CONVERTING_TABLE[dimension]


def get_corrected_size_and_dimension(value: float, dimension: str) -> (int, str):
    idx = UNITS.index(dimension)
    while value > 1023 and idx < 5:
        value /= 1024
        idx += 1
    return round(value), UNITS[idx]


data = {}

CONVERTING_TABLE = {
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
    'TB': 1024 ** 4,
}

UNITS = ('B', 'KB', 'MB', 'GB', 'TB')

with open('files.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        line = line.split()
        name = line[0]
        extension = line[0].split('.')[1]
        size, unit = int(line[1]), line[2]
        data.setdefault(extension, (),)
        data[extension] += (name, size, unit),

for k, v in sorted(data.items()):
    v = sorted(v, key=lambda x: x[0])
    sum_sizes_in_bytes = 0
    dimensions = set()
    for el in v:
        el_name = el[0]
        el_size = el[1]
        el_dimension = el[2]
        dimensions.add(el_dimension)
        if el_dimension != 'B':
            el_size = get_size_in_bytes(el_size, el_dimension)
        sum_sizes_in_bytes += el_size
        print(el_name)
    largest_dimension = ('GB' in dimensions and 'GB') or ('TB' in dimensions and 'TB') \
        or ('MB' in dimensions and 'MB') or ('KB' in dimensions and 'KB') or ('B' in dimensions and 'B')
    sum_sizes_in_largest_dimension = sum_sizes_in_bytes / CONVERTING_TABLE[largest_dimension]
    if sum_sizes_in_largest_dimension > 1023:
        sum_sizes_in_largest_dimension, largest_dimension = get_corrected_size_and_dimension(
            sum_sizes_in_largest_dimension, largest_dimension)

    print('----------')
    print(f'Summary: {round(sum_sizes_in_largest_dimension)} {largest_dimension}\n')

'''
------- test inputs -----
Sample Input 1:


Sample Input 2:


'''

'''
--------- expected outputs --------
Sample Output 1:


Sample Output 2:

'''