text = input().split()

my_dict = {}

for el in text:
    my_dict[el] = my_dict.get(el, 0) + 1
    print(my_dict[el], end=' ')