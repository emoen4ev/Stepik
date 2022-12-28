from decimal import *

num = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)

print(num)

if num == 0:
    print('YES')
else:
    print('NO')