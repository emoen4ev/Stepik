my_list = []
number = int(input())
for num in range(number):
    x = int(input())
    my_list.append(x)
print(*my_list, sep='\n')
print()
for x in my_list:
    x = x ** 2 + 2 * x + 1
    print(x, sep='\n')