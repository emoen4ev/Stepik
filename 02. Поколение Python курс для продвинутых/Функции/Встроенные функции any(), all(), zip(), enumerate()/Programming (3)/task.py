def is_valid_ip(data):
    upper_ip_limit = 255

    if len(data) != 4:
        return False

    return all(map(lambda element: element.isdecimal() and int(element) <= upper_ip_limit, data))


print(is_valid_ip(input().split('.')))