n = int(input())

commands_data = {}

commands_map = {
    'execute': 'X',
    'read': 'R',
    'write': 'W',
}

for _ in range(n):
    name, *commands = input().split()
    commands_data[name] = commands

m = int(input())

for _ in range(m):
    command, name = input().split()

    print('OK' if commands_map[command] in commands_data[name] else 'Access denied')