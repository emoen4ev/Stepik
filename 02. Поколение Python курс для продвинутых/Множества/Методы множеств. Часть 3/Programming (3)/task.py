grades_student_1 = set(input().split(' '))
grades_student_2 = set(input().split(' '))
grades_student_3 = set(input().split(' '))

same_grades_for_all = grades_student_1.intersection(grades_student_2, grades_student_3)

all_grades_for_all = grades_student_1.union(grades_student_2, grades_student_3)

result = all_grades_for_all.difference(same_grades_for_all)

result = sorted(int(_) for _ in result)

print(*result)