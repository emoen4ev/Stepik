def print_products(*args):
    counter = 0
    for element in args:
        if isinstance(element, str) and element:
            counter += 1
            print(f'{counter}) {element}')
    if counter == 0:
        print('Нет продуктов')


# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
#
# print_products([4], {}, 1, 2, {'Beegeek'}, '')