from functools import reduce

result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
print(result)