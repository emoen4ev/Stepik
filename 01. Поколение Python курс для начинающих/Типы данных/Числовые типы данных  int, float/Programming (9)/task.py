n = int(input())
dig_3 = n % 10
dig_2 = (n // 10) % 10
dig_1 = n // 100
min_dig = min(dig_1, dig_2, dig_3)
max_dig = max(dig_1, dig_2, dig_3)
if (max_dig - min_dig) == ((dig_1 + dig_2 + dig_3) - (max_dig + min_dig)):
    print("Число интересное")
else:
    print("Число неинтересное")




