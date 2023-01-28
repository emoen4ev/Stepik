number_ip_addresses = int(input())

data = [[int(x) for x in input().split('.')] for _ in range(number_ip_addresses)]

sorted_data = sorted(data, key=lambda x: x[0] * (256 ** 3) + x[1] * (256 ** 2) + x[2] * 256 + x[3])

for cur_ip in sorted_data:
    print('.'.join(str(number) for number in cur_ip))