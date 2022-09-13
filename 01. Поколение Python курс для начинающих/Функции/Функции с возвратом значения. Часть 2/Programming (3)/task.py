# объявление функции
def is_password_good(password):
    lowercase_letter = False
    uppercase_letter = False
    there_is_a_number = False

    if len(password) < 8:
        return False

    for char in password:
        if char.islower():
            lowercase_letter = True
        if char.isupper():
            uppercase_letter = True
        if char.isdigit():
            there_is_a_number = True

    return lowercase_letter and uppercase_letter and there_is_a_number


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))