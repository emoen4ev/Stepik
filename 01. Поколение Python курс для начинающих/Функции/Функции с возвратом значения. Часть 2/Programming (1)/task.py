# объявление функции
def is_prime_func(num):
    is_prime = False
    if num > 1:
        is_prime = True
        for k in range(2, num // 2 + 1):
            if num % k == 0:
                is_prime = False
                break

    return is_prime


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime_func(n))