year = int(input())
dig_4 = year % 10
dig_3 = (year // 10) % 10
if dig_4 == dig_3 == 0:
    print("YES")
else:
    print("NO")




