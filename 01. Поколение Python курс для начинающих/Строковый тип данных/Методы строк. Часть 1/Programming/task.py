# name = input()
# name_1 = name.title()
# if name == name_1:
#     print("YES")
# else:
#     print("NO")


# Тернарный оператор в Python:

name = input()
answer = "YES" if name == name.title() else "NO"
print(answer)

# name = input()
# answer = ("NO", "YES")[name == name.title()]
# print(answer)