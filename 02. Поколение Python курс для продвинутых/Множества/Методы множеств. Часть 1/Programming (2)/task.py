text = [word.lower().strip('.,;:-?!') for word in input().split()]

unique_words = set(text)

print(len(unique_words))