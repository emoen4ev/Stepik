def chunked(text, number):
    counter = 0
    result = []
    current = []

    for el in text:
        if counter < number:
            current.append(el)
            counter += 1
        else:
            result.append(current)
            current = [el]
            counter = 1

    result.append(current)

    return result


sequence = input().split()
n = int(input())

print(chunked(sequence, n))