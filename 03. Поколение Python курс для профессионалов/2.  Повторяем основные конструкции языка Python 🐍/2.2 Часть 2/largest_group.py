"""
---------- task 'largest_group'/ requirements --------
Назовем набор различных натуральных чисел группой. Например: (13,4,22,40).
Тогда длиной группы будем считать количество чисел в группе. Например, длина группы (13,4,22,40) равна 4.

Дана последовательность натуральных чисел от 1 до n включительно.
Напишите программу, которая группирует все числа данной последовательности по сумме их цифр и определяет длину группы,
содержащей наибольшее количество чисел.

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна сгруппировать все числа из натуральной последовательности от 1 до n по сумме их цифр
и определить длину группы, содержащей наибольшее количество чисел.

Примечание 1
Рассмотрим третий тест, в котором n=20.
Запишем последовательность чисел от 1 до 20: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
Сгруппируем полученные числа по сумме их цифр: (1,10),(2,11,20),(3,12),(4,13),(5,14),(6,15),(7,16),(8,17),(9,18),(19)
Итак, длина группы с наибольшим количеством чисел равна 3.
"""


def get_sum_digits(number: int) -> int:
    return sum(map(lambda x: int(x), str(number)))


n = int(input())

initial_sequence = [x for x in range(1, n + 1)]

data = {}

for el in initial_sequence:
    key = get_sum_digits(el)
    (key not in data and data.setdefault(key, [])) or data[key].append(el)

result = len(max(data.values(), key=lambda x: len(x)))

print(result)

'''
------- test inputs -----
Sample Input 1:
13

Sample Input 2:
2

Sample Input 3:
20

Sample Input 4:

'''

'''
--------- expected outputs --------
Sample Output 1:
2

Sample Output 2:
1

Sample Output 3:
3

Sample Output 4:


'''