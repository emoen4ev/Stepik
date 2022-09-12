text = input()

l_text = text.split(" ")

# for c in l_text:
#     c = int(c)
#     if c % 2 == 0 and (c ** 2) % 10 != 4:
#         print(c ** 2)

squares = [int(c) ** 2 for c in l_text if int(c) % 2 == 0 and int(c) ** 2 % 10 != 4]

print(*squares)