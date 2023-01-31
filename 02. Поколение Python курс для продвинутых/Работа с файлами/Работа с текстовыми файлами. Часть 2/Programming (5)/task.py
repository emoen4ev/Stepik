def get_number_letters(row):
    counter = 0
    for ch in row:
        counter += (0, 1)[ch.isalpha()]
    return counter


with open('file.txt', 'rt', encoding='utf-8') as file:
    letters = 0
    words = 0

    data = [line.strip() for line in file.readlines()]
    lines = len(data)

    for current_line in data:
        letters += get_number_letters(current_line)
        line = current_line.split()
        words += len(line)

result = f'''
Input file contains:
{letters} letters 
{words} words 
{lines} lines 
'''

print(result)

''' --- file.txt ---
A new report on the state of American youth says teenagers are very concerned about the direction their nation is taking.
They feel the upcoming presidential election will have as big impact on their lives, as the presidential election in 2004.
The survey released by the Horatio Alger Association of Distinguished Americans looked at the views of more than 1000 young people aged 13 to l9.
According to that study, 62 percent of the US teens believed the Kerry election in 2004 would make a large difference in the direction of the country and 70 percent said they cared who would win.
Allan Rivlin, a senior vice president with Peter Hart Research, says today young people are more involved with their society and know what is happening.
He notes, "They are paying attention to the Iraq war".
The young people surveyed also expressed concern over the employment and recession situation in America.
But Rivlin says their greatest area of apprehension "has to do with issues like gay marriage and abortion".
These social issues topped the list of concerns among the young.
One promising revelation of Rivlins report is that the US teenagers have a high opinion of their parents in general.
In the report, 77 percent of teens say they get along with their parents or guardians.
They have a great deal of admiration for their parents as well.
'''

'''
Input file contains:
1069 letters 
229 words 
12 lines 
'''