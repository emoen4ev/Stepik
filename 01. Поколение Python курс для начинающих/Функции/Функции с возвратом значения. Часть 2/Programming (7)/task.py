# объявление функции
def is_correct_bracket(text):
    counter = 0

    for x in text:
        if x == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False
    if counter == 0:
        return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))