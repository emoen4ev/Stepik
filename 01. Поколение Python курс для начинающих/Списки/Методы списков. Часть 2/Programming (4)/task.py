text = input()

text = text.split()
list_with_numbers = []

for number in text:
    number = int(number)
    list_with_numbers.append(number)

sorted_list = sorted(list_with_numbers)
reverse_sorted_list = sorted(list_with_numbers, reverse=True)

print(*sorted_list)
print(*reverse_sorted_list)
