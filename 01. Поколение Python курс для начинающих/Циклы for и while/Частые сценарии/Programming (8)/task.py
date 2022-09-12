n = int(input())
largest = 0
pre_largest = 0
for i in range(n):
    number = int(input())
    if number > largest:
        pre_largest = largest
        largest = number
    elif largest > number > pre_largest:
        pre_largest = number
print(largest, pre_largest, sep="\n")




