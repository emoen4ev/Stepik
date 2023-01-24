def mean(*args):
    s = tuple(x for x in args if type(x) in (int, float))

    return sum(s) / (len(s) or 1)


# https://stackoverflow.com/questions/47007680/how-do-and-and-or-act-with-non-boolean-values/47007761#47007761

# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))