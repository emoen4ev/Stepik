text = input()
counter = 0
while text not in ("стоп", "хватит", "достаточно"):
    counter += 1
    text = input()
print(counter)