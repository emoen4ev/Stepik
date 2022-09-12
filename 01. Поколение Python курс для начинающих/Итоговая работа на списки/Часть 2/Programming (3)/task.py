text = input()

numbers = text.split('-')

is_valid_phone_number = True

if 4 < len(numbers) or len(numbers) < 3:
    is_valid_phone_number = False

elif len(numbers) == 3:
    if len(numbers[0]) != 3 or not numbers[0].isdigit():
        is_valid_phone_number = False
    else:
        if len(numbers[1]) != 3 or not numbers[1].isdigit():
            is_valid_phone_number = False
        else:
            if len(numbers[2]) != 4 or not numbers[2].isdigit():
                is_valid_phone_number = False

elif len(numbers) == 4:
    if numbers[0] != '7':
        is_valid_phone_number = False
    else:
        if len(numbers[1]) != 3 or not numbers[1].isdigit():
            is_valid_phone_number = False
        else:
            if len(numbers[2]) != 3 or not numbers[2].isdigit():
                is_valid_phone_number = False
            else:
                if len(numbers[3]) != 4 or not numbers[3].isdigit():
                    is_valid_phone_number = False

if is_valid_phone_number:
    print('YES')
else:
    print('NO')
