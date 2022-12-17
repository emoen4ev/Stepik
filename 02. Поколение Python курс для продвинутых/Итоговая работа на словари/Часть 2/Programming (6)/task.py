n = int(input())

data_dict = {}

for _ in range(n):
    user, item, amount = input().split()

    data_dict[user] = data_dict.get(user, {})
    data_dict[user][item] = data_dict.get(user, {}).get(item, 0) + int(amount)

for user in sorted(data_dict):
    print(f'{user}:', sep='\n')
    for item in sorted(data_dict[user]):
        print(f'{item} {data_dict[user][item]}', sep='\n')