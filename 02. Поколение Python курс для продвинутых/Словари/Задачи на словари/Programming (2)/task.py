text_1, text_2 = input().lower(), input().lower()

my_dict = {}

for ch in text_1:
    if ch not in ' .,!?:;-':
        my_dict[ch] = my_dict.get(ch, 0) + 1

for ch in text_2:
    if ch not in ' .,!?:;-':
        my_dict[ch] = my_dict.get(ch, 0) - 1

print(('YES', 'NO')[any(my_dict[key] for key in my_dict)])