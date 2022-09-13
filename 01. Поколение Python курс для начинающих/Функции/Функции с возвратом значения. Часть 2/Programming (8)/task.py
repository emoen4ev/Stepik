# объявление функции
def convert_to_python_case(text):
    new_text = ''
    for idx, char in enumerate(text):
        if idx == 0 and char.isupper():
            new_text += char.lower()
        elif char.isupper():
            new_part = '_' + char.lower()
            new_text += new_part
        else:
            new_text += char.lower()

    return new_text


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))