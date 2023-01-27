def help_timur(number_of_classes):
    all_results = []

    for _ in range(number_of_classes):
        number_of_students = int(input())
        data = [input().split() for _ in range(number_of_students)]
        cur_class_result = any(int(x[1]) == 5 for x in data)
        all_results.append(cur_class_result)

    return ('NO', 'YES')[all(all_results)]


print(help_timur(int(input())))