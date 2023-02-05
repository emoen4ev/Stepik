from string import punctuation, ascii_lowercase


def get_new_character_index(symbol):
    current_symbol_index = lower_case_alphabet.index(symbol.lower())

    if direction == 'Right':
        new_symbol_index = current_symbol_index + step
        if new_symbol_index > k - 1:
            new_symbol_index -= k
    else:
        new_symbol_index = current_symbol_index - step

    return new_symbol_index


initial_text = input().split()

direction = 'Right'
# direction = 'Left'

# lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_case_alphabet = ascii_lowercase

k = len(lower_case_alphabet)

output_text = ''

for current_word in initial_text:
    step = len(current_word.strip(punctuation))
    for current_character in current_word:
        if current_character.lower() in lower_case_alphabet:
            new_character = lower_case_alphabet[get_new_character_index(current_character)]
            # if current_character.isupper():
            #     new_character = new_character.upper()
            # current_character = new_character
            current_character = (new_character, new_character.upper())[current_character.isupper()]
        output_text += current_character
    output_text += ' '

print(output_text)