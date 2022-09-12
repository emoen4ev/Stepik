number = int(input())
dig4 = number % 10
dig3 = (number // 10) % 10
dig2 = (number // 100) % 10
dig1 = number // 1000
print("Цифра в позиции тысяч равна", dig1)
print("Цифра в позиции сотен равна", dig2)
print("Цифра в позиции десятков равна", dig3)
print("Цифра в позиции единиц равна", dig4)





