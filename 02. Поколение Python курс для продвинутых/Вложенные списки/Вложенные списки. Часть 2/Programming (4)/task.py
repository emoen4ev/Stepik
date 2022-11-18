text = input().split()

result = []
current = []

for el in text:
    if not current or el in current:
        current.append(el)
    else:
        result.append(current)
        current = [el]

result.append(current)

print(result)