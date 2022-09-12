# text = input()
# counter = 0
# for i in range(len(text)):
#     if text[i] == text[i].lower() and text[i] not in "0123456789":
#         counter += 1
# print(counter)


text = input()
counter = 0
for c in text:
    if c != c.upper():
        counter += 1
print(counter)
