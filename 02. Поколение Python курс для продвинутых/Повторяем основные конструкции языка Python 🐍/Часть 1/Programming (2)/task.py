text = input()

price_for_char = 60
total_price = len(text) * price_for_char

r = total_price // 100
k = total_price % 100

print(f'{r} р. {k} коп.')