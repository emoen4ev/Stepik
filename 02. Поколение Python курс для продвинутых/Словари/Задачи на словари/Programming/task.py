n = int(input())

my_dict = {}

for _ in range(n):
    current_key, current_value = input().split(': ')

    my_dict[current_key.lower()] = current_value

m = int(input())

for _ in range(m):
    current_word = input().lower()
    print(my_dict.get(current_word, 'Не найдено'))