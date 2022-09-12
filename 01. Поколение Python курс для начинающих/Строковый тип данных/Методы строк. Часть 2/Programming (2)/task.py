n = int(input())

counter = 0

for i in range(n):
    text = input()
    k = text.count("11")
    if k >= 3:
        counter += 1

print(counter)