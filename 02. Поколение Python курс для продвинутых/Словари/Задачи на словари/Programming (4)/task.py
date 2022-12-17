n = int(input())

data_dict = {}

for _ in range(n):
    line = input().split()
    data_dict[line[0]] = line[1:]

m = int(input())

for _ in range(m):
    word = input()
    for k, v in data_dict.items():
        if word in v:
            print(k)
            break