def is_prime_func(num):
    is_prime = False
    if num > 1:
        is_prime = True
        for k in range(2, num // 2 + 1):
            if num % k == 0:
                is_prime = False
                break

    return is_prime


# объявление функции
def get_next_prime(num):
    while not is_prime_func(num):
        num += 1
    return num


# считываем данные
n = int(input())
n += 1

# вызываем функцию
print(get_next_prime(n))