from math import ceil

text = input()

x = ceil(len(text) / 2)

reverted_text = text[x:] + text[:x]

print(reverted_text)