with open('books.txt', 'w', encoding='utf-8') as file:
    li = '''Лев Толстой «Война и мир», Джордж Оруэлл «1984», Джеймс Джойс «Улисс», Владимир Набоков «Лолита», Уильям Фолкнер «Звук и ярость»'''.split(',')
    print(li)
    li2 = []
    for i in li:
        print(i)
        string = f"{i.strip()}\n" #'{}\n'.format(i.strip())
        li2.append(string)
    file.writelines(li2)

with open('books.txt', 'w', encoding='utf-8') as file:
    li = '''Лев Толстой «Война и мир», Джордж Оруэлл «1984», Джеймс Джойс «Улисс», Владимир Набоков «Лолита», Уильям Фолкнер «Звук и ярость»'''.split(',')
    file.writelines([f"{i.strip()}\n" for i in li])

with open('books.txt', 'w', encoding='utf-8') as file:
    li = '''Лев Толстой «Война и мир», Джордж Оруэлл «1984», Джеймс Джойс «Улисс», Владимир Набоков «Лолита», Уильям Фолкнер «Звук и ярость»'''.split(',')
    for i in li:
        print(i.strip(), file=file)

with open('file.txt', 'w', encoding='utf-8') as output:
    li = 'Лев Толстой «Война и мир», Джордж Оруэлл «1984», Джеймс Джойс «Улисс», Владимир Набоков «Лолита», Уильям Фолкнер «Звук и ярость»'.split(', ')
    print(*li, sep='\n', file=output)

with open('words.txt', 'w') as file:
    file.write('delphi+')
    file.write('java')