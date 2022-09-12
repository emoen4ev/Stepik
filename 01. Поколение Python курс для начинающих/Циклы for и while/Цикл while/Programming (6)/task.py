price = int(input())
amount_of_coins = 0
remaining_amount = price
while remaining_amount > 0:
    if 1 <= price < 5:
        amount_of_coins = price
        remaining_amount = 0
    elif 5 <= price < 10:
        amount_of_coins = price // 5 + price % 5
        remaining_amount = 0
    elif 10 <= price < 25:
        amount_of_coins = price // 10 + (price % 10) // 5 + (price % 10) % 5
        remaining_amount = 0
    else:
        amount_of_coins = price // 25 + (price % 25) // 10 + ((price % 25) % 10) // 5 + ((price % 25) % 10) % 5
        remaining_amount = 0
print(amount_of_coins)