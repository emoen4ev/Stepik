n = int(input())

data = tuple(input().split() for i in range(n))

# result = dict(data)

result = {x[0]: x[1] for x in data}

word = input()

for k, v in result.items():
    if word in k:
        print(v)
    elif word in v:
        print(k)