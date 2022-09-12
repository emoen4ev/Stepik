text = input()
digits = "0123456789"
counter = 0

for c in text:
    for d in digits:
        if c == d:
            counter += 1

print(counter)