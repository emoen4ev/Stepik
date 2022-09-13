ip = input()

ip_in_list = ip.split('.')

for number in ip_in_list:
    number = int(number)
    if number < 0 or number > 255:
        print("НЕТ")
        break
else:
    print("ДА")
