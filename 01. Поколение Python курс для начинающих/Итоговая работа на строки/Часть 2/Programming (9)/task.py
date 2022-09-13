text = input()

counter = text.count("f")

if counter == 0:
    print(-2)
elif counter == 1:
    print(-counter)
else:
    index = text.index("f", text.index("f") + 1)
    print(index)


# counter =0
#
# for i in range(len(text)):
#     if text[i] == "f":
#         counter += 1
#         if counter == 2:
#             print(i)
#
# if counter == 1:
#     print(-counter)
# elif counter == 0:
#     print(-2)