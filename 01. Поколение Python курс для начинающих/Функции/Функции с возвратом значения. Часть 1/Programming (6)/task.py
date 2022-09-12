def quick_merge(data_1, data_2):
    result_data = []

    p_1 = 0
    p_2 = 0

    while p_1 < len(data_1) and p_2 < len(data_2):
        if data_1[p_1] <= data_2[p_2]:
            result_data.append(data_1[p_1])
            p_1 += 1
        else:
            result_data.append(data_2[p_2])
            p_2 += 1

    if p_1 < len(data_1):
        result_data += data_1[p_1:]
    if p_2 < len(data_2):
        result_data += data_2[p_2:]

    return result_data


number_lines = int(input())

current_result = []
result = []

for i in range(number_lines):
    if i == 0:
        current_result = ([int(x) for x in input().split()])
    elif i > 0:
        current_data = ([int(x) for x in input().split()])
        result = quick_merge(current_result, current_data)
        current_result = result

print(*result, sep=' ')