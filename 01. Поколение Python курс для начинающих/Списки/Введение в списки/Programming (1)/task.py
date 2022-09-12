n = int(input())

text = ""

for i in range(97, 97 + n):
    text = text + chr(i)

chars = list(text)

print(chars)

