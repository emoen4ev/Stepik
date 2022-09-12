# объявление функции
def is_valid_password(password):
    data = password.split(':')

    if len(data) != 3:
        return False

    num_1, num_2, num_3 = data

    if num_1 != num_1[::-1]:
        return False

    if int(num_3) % 2 != 0:
        return False

    num_2 = int(num_2)

    if num_2 > 1:
        for x in range(2, num_2 // 2 + 1):
            if num_2 % x == 0:
                return False

    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))