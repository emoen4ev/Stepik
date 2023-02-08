"""
---------- task / requirements --------
Функция filter_anagrams()

Анаграммы — это слова, которые состоят из одинаковых букв. Например:
адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка

Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
- word — слово в нижнем регистре
- words — список слов в нижнем регистре

Функция должна возвращать список, элементами которого являются слова из списка words,
которые представляют анаграмму слова word.
Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. Считайте, что слово является анаграммой самого себя.
"""


from typing import List


def filter_anagrams(control_word: str, sequence: list) -> List[str]:
    sorted_control_word = sorted(control_word)

    return [element for element in sequence if sorted(element) == sorted_control_word]

    # return list(filter(lambda x: sorted(x) == sorted_control_word, sequence))

    # sorted_control_word = ''.join(sorted(control_word))    #
    # return list(filter(lambda x: ''.join(sorted(x)) == sorted_control_word, sequence))


# ------- test inputs -----
word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, anagrams))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

print(
    filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

print(filter_anagrams('стекло', []))

'''
--------- expected outputs --------
['aabb', 'bbaa']
['сеточка', 'стоечка', 'тесачок', 'чесотка']
['iamlordvoldemort']
[]
'''