word = 'beegeek'
set1 = set(word*3)
set2 = set(word[::-1]*2 + 'stepik')

print(set1)
print(set2)


print(set1 < set2)