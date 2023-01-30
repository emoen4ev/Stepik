def get_items_value(number, price):
    return number * price


file = open('prices.txt', 'rt', encoding='utf-8')

data = [line.split() for line in file.readlines()]

# print(data)

result = 0

for item in data:
    number_of_products = int(item[1])
    price_of_one_piece = int(item[2])

    result += get_items_value(number_of_products, price_of_one_piece)

print(result)

file.close()