text = input()

# for c in text:
#     if c.isdigit():
#         print(c, end='')

digits_in_text = [c for c in text if c.isdigit()]

print(*digits_in_text, sep='')