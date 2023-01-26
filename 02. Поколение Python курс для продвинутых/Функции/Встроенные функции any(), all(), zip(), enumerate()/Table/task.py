print(all([True, False]))
print(all([False, False]))
print(all([True, True]))
print(all([10, 100, 1000]))
print(all([10, 100, 0, 1000]))
print(all(['Python', 'C#']))
print(all(['school', '', 'language']))
print(all([(1, 2, 3), []]))
print(all([]))
print(all([[], []]))
print(all({0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}))
print(all({'name': 'Timur', 'age': 28}))
print(all({'': 'None', 'age': 28}))


def all_1(iterable):
    for item in iterable:
       if not item:
           return False
    return True

print(all_1([]))