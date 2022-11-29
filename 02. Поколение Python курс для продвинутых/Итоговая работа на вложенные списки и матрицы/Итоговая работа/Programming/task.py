text = input().split()

n = int(input())

result = [[] * i for i in range(n)]

for i in range(len(text)):
    result[i % n].append(text[i])

print(result)