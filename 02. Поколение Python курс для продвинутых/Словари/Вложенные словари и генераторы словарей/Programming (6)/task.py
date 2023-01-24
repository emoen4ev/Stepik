words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {el: [ord(ch) for ch in el] for el in words}

# print(result)