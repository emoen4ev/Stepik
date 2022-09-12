text_with_numbers = input()

list_with_numbers = text_with_numbers.split()
counter = 0

for i in range(len(list_with_numbers) - 1):
    for j in range(i + 1, len(list_with_numbers)):
        if int(list_with_numbers[j]) == int(list_with_numbers[i]):
            counter += 1

print(counter)
