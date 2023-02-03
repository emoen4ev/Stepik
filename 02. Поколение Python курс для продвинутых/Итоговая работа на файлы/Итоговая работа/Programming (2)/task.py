low_limit = 64
result = 0

with open('grades.txt', 'rt', encoding='utf-8') as input_file:
    data = [x.strip().split() for x in input_file]

    for current_student in data:
        grade_1, grade_2, grade_3 = [int(x) for x in current_student[1:]]
        condition = grade_1 > low_limit and grade_2 > low_limit and grade_3 > low_limit
        result += 1 if condition else 0

print(result)