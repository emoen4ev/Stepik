def greet(name, *args):
    return f"Hello, {name}{('', ' and ')[1 if args else 0]}{' and '.join(current_name for current_name in args)}!"


# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))