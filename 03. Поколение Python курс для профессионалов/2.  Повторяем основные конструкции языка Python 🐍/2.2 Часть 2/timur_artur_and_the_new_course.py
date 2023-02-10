"""
---------- task / requirements --------
Сегодня Тимур ждёт в гости своего друга Артура, чтобы спланировать работу по новому курсу "ООП на Python".
Чтобы подготовиться к встрече, Тимуру необходимо посетить два магазина, расположенных рядом с его домом.
От дома до первого магазина ведёт дорожка длиной d1 метров, а до второго магазина ведёт дорожка длиной d2 метров.
Также существует дорожка, соединяющая два магазина друг с другом, длиной d3 метров.

Напишите программу, которая вычисляет минимальное расстояние, которое потребуется пройти Тимуру,
чтобы посетить оба магазина и вернуться домой. Тимур всегда стартует из дома. Он должен посетить оба магазина,
перемещаясь только по имеющимся трём дорожкам, и вернуться назад домой. При этом его совершенно не смутит,
если ему придётся посетить один и тот же магазин или пройти по одной и той же дорожке более одного раза.
Единственная его задача — минимизировать суммарное пройденное расстояние.

Формат входных данных
На вход программе подаются 3 натуральных числа d1, d2, d3 — длины дорожек, каждое на отдельной строке:
- d1 — длина дорожки, соединяющая дом Тимура и первый магазин
- d2 — длина дорожки, соединяющая дом Тимура и второй магазин
- d3 — длина дорожки, соединяющая магазины

Формат выходных данных
Программа должна вывести минимальное количество метров, которое придётся пройти Тимуру, чтобы посетить оба магазина
и вернуться домой.


Примечание 1. Первый пример изображён на рисунке: https://stepik.org/lesson/569749/step/1?unit=564263

Одним из оптимальных маршрутов является: дом ⟶ первый магазин ⟶ второй магазин ⟶ дом.

Во втором примере одним из оптимальных маршрутов является: дом ⟶ первый магазин ⟶ дом ⟶ второй магазин ⟶ дом.
"""

distances = [int(input()) for _ in range(3)]

sorted_distances = sorted(distances)

# result = min((sorted_distances[0] + sorted_distances[1]) * 2, sum(distances))
result = min(sum(sorted_distances[:2]) * 2, sum(distances))

print(result)

'''
------- test inputs -----
Sample Input 1:
10
20
30

Sample Input 2:
10
10
45

Sample Input 3:
100
33
34

Sample Input 4:
777
777
777
'''

'''
--------- expected outputs --------
Sample Output 1:
60

Sample Output 2:
40

Sample Output 3:
134

Sample Output 4:
2331
'''