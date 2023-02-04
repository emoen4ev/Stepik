file_name = input()
# file_name = 'test.txt'

comment = False
is_best_team = True

with open(file_name, 'rt') as input_file:
    for line in input_file:
        if line.startswith('#'):
            comment = True
        elif line.startswith('def ') and not comment:
            idx = line.index('(')
            print(line[4:idx])
            is_best_team = False
        elif line.startswith('def ') and comment:
            comment = False

    if is_best_team:
        print('Best Programming Team')