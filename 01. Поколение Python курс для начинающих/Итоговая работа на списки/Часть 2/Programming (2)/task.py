initial_text_with_numbers = input()

new_text = initial_text_with_numbers.replace(' ', '+', len(initial_text_with_numbers) - 1)

sum_numbers = 0

list_new_text = new_text.split('+')

for number in list_new_text:
    sum_numbers += int(number)

print(f"{new_text}={sum_numbers}")
