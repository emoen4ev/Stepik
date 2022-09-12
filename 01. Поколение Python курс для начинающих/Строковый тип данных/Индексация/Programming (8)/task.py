text = input()
counter = 0
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        counter += 1
print(counter)