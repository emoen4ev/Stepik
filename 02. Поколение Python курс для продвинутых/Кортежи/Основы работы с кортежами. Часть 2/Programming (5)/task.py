n = int(input())

listing = ()

for _ in range(n):
    cur = tuple(input().split())
    listing += cur,

for el in listing:
    print(*el, end='\n')

print()

for el in listing:
    if int(el[1]) > 3:
        print(*el, end='\n')