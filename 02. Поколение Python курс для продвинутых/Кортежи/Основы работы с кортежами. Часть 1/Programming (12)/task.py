tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]

new_tuples = []

for el in tuples:
    new_el = el[:-1] + (100,)
    new_tuples.append(new_el)

print(new_tuples)