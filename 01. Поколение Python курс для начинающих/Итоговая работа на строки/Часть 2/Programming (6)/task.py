text = input()

for i in range(len(text)):
    if i % 3 == 0:
        continue
    print(text[i], end='')