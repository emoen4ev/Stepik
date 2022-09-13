# объявление функции
def is_palindrome(text):
    new_text = ''.join(x.lower() for x in text if x.isalnum())
    return new_text == new_text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))