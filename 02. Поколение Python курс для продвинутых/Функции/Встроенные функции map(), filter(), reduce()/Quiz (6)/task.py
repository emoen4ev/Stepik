list1 = list(map(len, ['this', 'is', 'a', 'test']))
list2 = [len(word) for word in ['this', 'is', 'a', 'test']]

print(list1 == list2)