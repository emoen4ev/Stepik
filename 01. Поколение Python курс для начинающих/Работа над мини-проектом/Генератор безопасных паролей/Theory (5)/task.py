import random, string


def logo():
    part_1 = '\n' + 18 * ' ' + 17 * '+' + '\n'
    part_2 = 'Smart Password Generator v.1.0 ... powered by Emo ...'
    return part_1 + part_2 + part_1 + '\n'


def confirm_is_digit(data):
    while True:
        if data.isdigit():
            return int(data)
        else:
            data = input('Please, enter a number ... !' + '\n')
            continue


def confirm_y_or_n(data):
    while True:
        if data == 'y':
            return True
        if data == 'n':
            return False
        else:
            data = input("Please, enter 'y' or 'n'...!" + '\n').lower().strip()
            continue


def generate_password(length: int, chars: list):
    pass


def run():
    possible_chars = ''

    while True:
        number_passwords = input('How many passwords do you want to generate for you ... ?' + '\n').strip()
        number_passwords = confirm_is_digit(number_passwords)
        if number_passwords == 0:
            print('Ok, ... bye ...')
            break

        allow_lowercase = input("Should I use lowercase letters in the password?  'y' or 'n' ... ?" + '\n'). \
            lower().strip()
        allow_lowercase = confirm_y_or_n(allow_lowercase)
        if allow_lowercase:
            possible_chars += lowercase_letters

        allow_uppercase = input("And uppercase letters ... ?  'y' or 'n' ... ?" + '\n').lower().strip()
        allow_uppercase = confirm_y_or_n(allow_uppercase)
        if allow_uppercase:
            possible_chars += uppercase_letters

        allow_digits = input("Do you want digits ... ?  'y' or 'n' ... ?" + '\n').lower().strip()
        allow_digits = confirm_y_or_n(allow_digits)
        if allow_digits:
            possible_chars += digits

        allow_punctuations = input(
            "Аnd about the punctuation characters, what do you think, should I include them ...?  'y' or 'n'" + '\n'). \
            lower().strip()
        allow_punctuations = confirm_y_or_n(allow_punctuations)
        if allow_punctuations:
            possible_chars += punctuation_characters

        allow_ambiguous = input(
            "And now be careful - should I use ambiguous characters, like 'il1Lo0O' ...?  'y' or 'n'" + '\n'). \
            lower().strip()
        allow_ambiguous = confirm_y_or_n(allow_ambiguous)

        if allow_ambiguous:
            possible_chars = list(possible_chars)
        else:
            possible_chars = [char for char in possible_chars if char not in ambiguous_characters]

        pass_long = input('And lastly - how many characters you want the password to be long?' + '\n')
        pass_long = confirm_is_digit(pass_long)
        if pass_long == 0:
            print('Ok, ... bye ...')
            break


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
punctuation_characters = string.punctuation
ambiguous_characters = 'il1Lo0O'

print(logo())

run()