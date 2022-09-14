first_text = input().split(' ')
second_text = input().split(' ')

L = []
M = []
list_with_sum = []

for number in first_text:
    L.append(number)

for number in second_text:
    M.append(number)

for j in range(len(L)):
    current_number_j = int(L[j])
    for m in range(j, len(M)):
        current_number_m = int(M[m])
        sum_numbers = current_number_j + current_number_m
        list_with_sum.append(sum_numbers)
        break

print(*list_with_sum)
