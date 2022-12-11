grades_student_1 = set(input().split(' '))
grades_student_2 = set(input().split(' '))
grades_student_3 = set(input().split(' '))

result = grades_student_3.difference(grades_student_1,grades_student_2)

result = sorted((int(_) for _ in result), reverse=True)

print(*result)