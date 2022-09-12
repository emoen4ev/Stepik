counter = 0
for i in range(10):
    number = int(input())
    if number % 2 == 0:
        counter += 1
if counter == 10:
    print("YES")
else:
    print("NO")