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


def convert_word(current_word):
    for ch in current_word:
        current_word = (ch in vowel_letters and current_word.replace(ch, '0')) or current_word.replace(ch, '1')
    return current_word


initial_control_word = input()
number_words = int(input())

data = [input() for _ in range(number_words)]

vowel_letters = 'ауоыиэяюёе'
consonants = 'бвгджзйклмнпрстфхцчшщ'
control_word = convert_word(initial_control_word)
k = len(control_word)

for word in data:
    if control_word == convert_word(word[:k]):
        print(word)

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