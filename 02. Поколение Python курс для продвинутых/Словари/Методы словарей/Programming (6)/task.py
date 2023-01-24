text = input().split()

result = {}

for symbol in text:
    if symbol not in result:
        result[symbol] = 0
    else:
        result[symbol] += 1

    print(symbol if int(result[symbol]) == 0 else f'{symbol}_{result[symbol]}', end=' ')