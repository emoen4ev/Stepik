course_id = input()

courses_data = {
    'CS101': (3004, 'Хайнс', '8:00'),
    'CS102': (4501, 'Альварадо', '9:00'),
    'CS103': (6755, 'Рич', '10:00'),
    'NT110': (1244, 'Берк', '11:00'),
    'CM241': (1411, 'Ли', '13:00'),
}

if course_id in courses_data:
    print(f'{course_id}: {courses_data[course_id][0]}, {courses_data[course_id][1]}, {courses_data[course_id][2]}')