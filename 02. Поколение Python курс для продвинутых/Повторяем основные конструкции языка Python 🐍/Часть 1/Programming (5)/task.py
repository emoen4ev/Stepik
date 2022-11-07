# number = input()
# print(int(number[:-5] + number[-5:][::-1]))

number = input()
if len(number) == 5:
    print(int(number[::-1]))
else:
    print(int(number[0] + number[5:0:-1]))