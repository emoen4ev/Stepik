with open('lines.txt', 'rt', encoding='utf-8') as file:
    data = [line.strip() for line in file.readlines()]
    sorted_by_length = sorted(data, key=lambda line: -len(line))
    greatest_length = len(sorted_by_length[0])
    result= filter(lambda line: len(line) == greatest_length, sorted_by_length)

print(*result, sep='\n')




'''
future belongs
to those who
believe in their..
dreams
Life begins
at the end
of your comfort
zone
Life is what 12345
happens while you
are busy making
other plans
Beautiful is
better than ugly!!
Explicit is better
than implicit
Simple is better
than complex
Complex is better
than complicated
'''