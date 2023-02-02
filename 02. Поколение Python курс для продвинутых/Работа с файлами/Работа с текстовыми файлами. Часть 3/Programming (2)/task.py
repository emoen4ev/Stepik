with open('input.txt', 'rt', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    data = input_file.readlines()

# with open('output.txt', 'w', encoding='utf-8') as output_file:
    # for i in range(len(data)):
    #     current_data = f'{i + 1}) {data[i]}'
    #     print(current_data, end='', file=output_file)

    # print(*[f'{i + 1}) {data[i].strip()}' for i in range(len(data))], sep='\n', file=output_file)

    # for idx, value in enumerate(data):
    #     current_data = f'{idx + 1}) {value}'
    #     print(current_data, end='', file=output_file)

    print(*[f'{idx + 1}) {value.strip()}' for idx, value in enumerate(data)], sep='\n', file=output_file)

# with open('output.txt', 'rt', encoding='utf-8') as file:
#     control_data = file.readlines()
#
# print(control_data)

''' ------------------------ input.txt ------------------------
abcd
xcnvmnvkje
32432423
sdflsdjkn34r43
345349854395#$%$#
jksdfkjsdfkjsd
lwerjlwerlkwe
jwfhjkwehkjwefkjwebfjkwe
djdddddddddddddddddddddddddddddddd
3249835438594390583490583490853490582349058340
sdfsjkldflksdjaflkjsdflkjsdlfkjsdlfjsldfsldkfjlsdkfjls
'''