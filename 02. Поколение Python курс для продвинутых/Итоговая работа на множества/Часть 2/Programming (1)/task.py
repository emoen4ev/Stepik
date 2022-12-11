initial_data = list(map(int, input().split()))

minimum_data = set(initial_data)

result = len(initial_data) - len(minimum_data)

print(result)