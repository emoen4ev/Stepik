"""
---------- task / requirements --------
В русском и английском языках есть буквы, которые выглядят одинаково. Вот список английских букв "AaBCcEeHKMOoPpTXxy",
а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". Напишите программу, которая для трёх букв из данных списков букв
определяет, русские они, английские или и те и другие (смесь русских и английских букв).

Формат входных данных:
На вход программе подаются три буквы из указанных в условии наборов букв, каждая на отдельной строке.

Формат выходных данных:
Программа должна вывести
- ru, если все три буквы русские
- en, если все три буквы английские
- mix, если среди букв есть как русские, так и английские

Примечание 1:
Гарантируется, что введенные три буквы находятся в наборе "AaBCcEeHKMOoPpTXxy" + "АаВСсЕеНКМОоРрТХху",
(английские + русские буквы).
"""

en_letters = set('AaBCcEeHKMOoPpTXxy')
ru_letters = set('АаВСсЕеНКМОоРрТХху')

letters_for_check = {input() for _ in range(3)}

result = (letters_for_check.issubset(en_letters) and 'en') or (letters_for_check.issubset(ru_letters) and 'ru') \
         or (1 and 'mix')
print(result)


# if letters_for_check.issubset(en_letters):
#     print('en')
# elif letters_for_check.issubset(ru_letters):
#     print('ru')
# else:
#     print('mix')


# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])

'''
------- test inputs -----
Sample Input 1:
Р
О
А

Sample Input 2:
o
K
M

Sample Input 3:
T
а
B

Sample Input 4:

'''

'''
--------- expected outputs --------
Sample Output 1:
ru

Sample Output 2:
en

Sample Output 3:
mix

Sample Output 4:

'''