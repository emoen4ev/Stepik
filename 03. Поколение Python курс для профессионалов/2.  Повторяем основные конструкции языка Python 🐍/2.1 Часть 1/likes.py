"""
---------- task / requirements --------
Функция likes()

В различных социальных сетях существуют системы лайков, которые в зависимости от количества людей, оценивших запись,
показывают соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:
- names — список имён

Функция должна возвращать строку в соответствии с примерами ниже, содержание которой зависит от количества имён
в списке names.
"""


def likes(names: list) -> str:
    if not names:
        return 'Никто не оценил данную запись'

    length = len(names)
    if length == 1:
        return f'{names[0]} оценил(а) данную запись'
    if length == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    if length == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'

    return f'{names[0]}, {names[1]} и {length - 2} других оценили данную запись'


# ------- test inputs -----
print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))

print(likes(['Дима', 'Алиса']))
print(likes(['Эндрю', 'Тоби', 'Том']))
print(likes([]))

'''
--------- expected outputs --------
Никто не оценил данную запись
Тимур оценил(а) данную запись
Тимур и Артур оценили данную запись
Тимур, Артур и Руслан оценили данную запись
Тимур, Артур и 2 других оценили данную запись
Тимур, Артур и 3 других оценили данную запись
Тимур, Артур и 6 других оценили данную запись

Дима и Алиса оценили данную запись
Эндрю, Тоби и Том оценили данную запись
Никто не оценил данную запись
'''