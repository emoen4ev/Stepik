text = input()

counter = text.count("f")

if counter == 0:
    print("NO")
elif counter == 1:
    print(text.find("f"))
elif counter > 1:
    first_index = text.find("f")
    last_index = text.rfind("f")
    print(first_index, last_index)