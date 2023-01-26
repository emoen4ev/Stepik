from functools import reduce


def pretty_print(data, side='-', delimiter='|'):
    number_delimiters = len(data)
    number_spaces = len(data) + number_delimiters - 1
    number_sides = reduce(lambda x, y: x + (len(str(y)) if type(y) == int else len(y)), data,
                          0) + number_delimiters + number_spaces
    info_row = (' ' + delimiter + ' ').join(str(x) if type(x) == int else x for x in data)
    rows = [
        f' {side * number_sides} ',
        f'{delimiter} {info_row} {delimiter}',
        f' {side * number_sides} ',
    ]

    print('\n'.join(rows))


# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')