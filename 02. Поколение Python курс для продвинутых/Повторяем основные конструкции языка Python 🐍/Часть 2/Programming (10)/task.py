control_word = input()
other_text = ' ' + 'запретил букву'

text = (control_word + other_text).split()

all_chars = ''.join(text)

unique_chars = ''
result = ''

for ch in all_chars:
    if ch not in unique_chars:
        unique_chars += ch

unique_chars_sorted = ''.join(sorted(unique_chars))

for el in unique_chars_sorted:
    new_text = []
    for word in text:
        result += (word + ' ').lstrip()
        if el in word:
            word = word.replace(el, '')
        new_text.append(word)
    text = new_text
    print(result + el, end='\n')
    result = ''