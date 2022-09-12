# объявление функции
def get_shipping_cost(quantity):
    result = 1000 + 120 * (quantity - 1)
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))