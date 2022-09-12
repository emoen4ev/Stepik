import random, string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
punctuation_characters = string.punctuation
ambiguous_characters = 'il1Lo0O'

print('\n' + 17 * ' ' + 17 * '+')
print('Smart Password Generator v.1.0 ... powered by Emo ...')
print(17 * ' ' + 17 * '+' + 2 * '\n')

number_passwords = int(input('How many passwords do you want to generate for you ... ?' + '\n'))
includes_lowercase = input("Should I use lowercase letters in the password?  'y' or 'n' ... ?" + '\n')
includes_uppercase = input("And uppercase letters ... ?  'y' or 'n' ... ?" + '\n')
includes_digits = input("Do you want digits ... ?  'y' or 'n' ... ?" + '\n')
includes_punctuations = input(
    "Аnd about the punctuation characters, what do you think, should I include them ...?  'y' or 'n'" + '\n')
includes_ambiguous = input(
    "And now be careful - should I insert ambiguous characters, like 'il1Lo0O' ...?  'y' or 'n'" + '\n')