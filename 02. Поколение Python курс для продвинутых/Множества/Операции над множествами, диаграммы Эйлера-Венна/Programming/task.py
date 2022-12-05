sea_students = int(input())
village_students = int(input())
mountains_students = int(input())
sea_village_students = int(input())
mountains_village_students = int(input())
no_vacation_students = int(input())

vacationing_students = sea_students + village_students + mountains_students \
                       - sea_village_students - mountains_village_students

all_students = vacationing_students + no_vacation_students

print(all_students)