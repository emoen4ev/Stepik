numbers_word = int(input())

all_chars = ''

while numbers_word:
    current_word = input().lower()
    all_chars += current_word

    numbers_word -= 1

unique_chars = set(all_chars)

print(len(unique_chars))