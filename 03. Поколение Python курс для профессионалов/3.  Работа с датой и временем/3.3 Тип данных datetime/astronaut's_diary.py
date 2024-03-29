"""
Дневник космонавта 🌶️

Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день.
Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец.
Все отчеты разделены между собой пустой строкой.
Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM,
после которой следуют события, произошедшие за указанный день:

29.04.2006; 06:55
It wasn't until several hours after launch that we were able to take the time to get out of our seats
and enter the “habitation module.”
Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

03.05.2006; 20:24
Everybody had a sleeping bag although I only used mine on a couple of brief occasions,
and then only when getting a little chilly.
...

Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат.

Примечание 1. Например, если бы файл diary.txt имел вид:

13.02.1994; 18:49
Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».

03.02.1994; 20:18
Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
Она немного говорит по-русски и очень приятно слышать родную речь.

12.02.1994; 17:17
Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
Все это наводит на грустные размышления о нашей безалаберности и разрухе.

то программа должна была бы вывести:

03.02.1994; 20:18
Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
Она немного говорит по-русски и очень приятно слышать родную речь.

12.02.1994; 17:17
Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
Все это наводит на грустные размышления о нашей безалаберности и разрухе.

13.02.1994; 18:49
Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».

Примечание 2. Указанный файл(diary.txt) доступен по ссылке. Ответ на задачу(clue.txt) доступен по ссылке.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.
"""

from datetime import datetime

# dates_and_texts = []
# current_date = None
# stored_date = None
# current_text = ""
#
# with open('diary.txt', 'rt', encoding='utf-8') as file:
#     for line in file:
#         try:
#             current_date = datetime.strptime(line.strip(), "%d.%m.%Y; %H:%M")
#             if current_text != "":
#                 dates_and_texts.append((stored_date, current_text))
#                 current_text = ""
#         except ValueError:
#             current_text += line
#             stored_date = current_date
#
# dates_and_texts.append((current_date, current_text))
#
# dates_and_texts = sorted(dates_and_texts, key=lambda x: x[0])
#
# for date, text in dates_and_texts:
#     print(date.strftime("%d.%m.%Y; %H:%M"))
#     print(text.strip() + '\n')

# ----------------------------------------------------------------

# dates_and_texts = {}

# with open('diary.txt', 'rt', encoding='utf-8') as file:
#     for line in file:
#         line = line.strip()
#         try:
#             current_date = datetime.strptime(line, "%d.%m.%Y; %H:%M")
#             dates_and_texts.setdefault(current_date, [])
#         except ValueError:
#             line.strip() and dates_and_texts[current_date].append(line)
#
# l = len(dates_and_texts) - 1
#
# for idx, (date, text) in enumerate(sorted(dates_and_texts.items())):
#     print(date.strftime("%d.%m.%Y; %H:%M"), '\n'.join(text), sep='\n')
#     idx < l and print()

# ----------------------------------------------------------------

dates_and_texts = {}

with open('diary.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        try:
            current_date = datetime.strptime(line, "%d.%m.%Y; %H:%M")
            dates_and_texts.setdefault(current_date, (),)
        except ValueError:
            if line:
                dates_and_texts[current_date] += (line,)

l = len(dates_and_texts) - 1

for idx, (date, text) in enumerate(sorted(dates_and_texts.items())):
    print(date.strftime("%d.%m.%Y; %H:%M"), '\n'.join(text), sep='\n')
    idx < l and print()