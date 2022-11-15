text = input()

counter = 0
result = 0

for ch in text:
    if ch == 'Р':
        counter += 1
    else:
        if counter > result:
            result = counter
        counter = 0

print(max(result, counter))