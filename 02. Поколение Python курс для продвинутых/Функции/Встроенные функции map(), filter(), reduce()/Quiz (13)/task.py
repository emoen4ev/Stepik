from operator import add
from functools import reduce

result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)