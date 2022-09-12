# text = input()
# inverted_text = text[::-1]
# if text == inverted_text:
#     print("YES")
# else:
#     print("NO")

text = input()

a = ("NO", "YES")[text == text[::-1]]

print(a)
