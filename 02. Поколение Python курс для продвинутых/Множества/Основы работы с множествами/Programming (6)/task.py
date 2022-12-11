sec_1 = input()
sec_2 = input()

sec = set(sec_1 + sec_2)

print(('YES', 'NO')[len(sec) != 10])