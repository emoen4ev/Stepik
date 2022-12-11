grades_student_1, grades_student_2, grades_student_3 = [set(map(int, input().split())) for _ in range(3)]

grades_for_all = grades_student_1.union(grades_student_2, grades_student_3)

possible_grades = set(_ for _ in range(11))

result = possible_grades.difference(grades_for_all)

result = sorted(result)

print(*result)