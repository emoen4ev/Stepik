"""
--------- task / requirements --------------
Реализуйте функцию hide_card(), которая принимает один аргумент:
card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр, между которыми могут
присутствовать символы пробела. Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать
полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hide_card(), но не код,
вызывающий ее.
"""


def hide_card(card_number: str) -> str:
    card_number = card_number.replace(' ', '')
    card_number = '*' * 12 + card_number[12:]

    return card_number


# -------- test input ------------
card = '905 678123 45612 56'
print(hide_card(card))

'''  ---------  expected output  ------------
************1256
'''