"""
---------- task 'similar_words'/ requirements --------
Напишите программу, которая находит все схожие слова для заданного слова.
Слова называются схожими, если имеют одинаковое количество и расположение гласных букв.
При этом сами гласные могут различаться.

Формат входных данных:
На вход программе подается одно слово, записанное в первой строке,
затем натуральное число n — количество слов для сравнения и n строк со словами.

Формат выходных данных:
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.

Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.

Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е)
и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
"""


def get_pattern(current_word: str) -> list:
    pattern = [i for i, c in enumerate(current_word) if c in vowel_letters]
    return pattern


initial_control_word = input()
number_words = int(input())

vowel_letters = set('ауоыиэяюёе')
data = [input() for _ in range(number_words)]

control_word = get_pattern(initial_control_word)

for word in data:
    converted_word = get_pattern(word)
    if control_word == converted_word:
        print(word)

# vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)

'''
------- test inputs -----
Sample Input 1:
машина
8
сеть
машинист
дорога
урок
работа
аксиома
железо
ветеран

Sample Input 2:
весть
3
месть
гость
лань

Sample Input 3:


Sample Input 4:

'''

'''
--------- expected outputs --------
Sample Output 1:
машинист
дорога
работа
железо
ветеран

Sample Output 2:
месть
гость
лань

Sample Output 3:


Sample Output 4:

'''