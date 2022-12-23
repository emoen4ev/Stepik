import random

n = int(input())

users = [input() for _ in range(n)]

users_copy = users

vv = []

for user in users:
    ll = users_copy.pop(users.index(user))
    print(f'{user} - {random.choice(users_copy)}')