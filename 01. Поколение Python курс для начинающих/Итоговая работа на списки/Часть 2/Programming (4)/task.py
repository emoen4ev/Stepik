# text = input()

# l_text = input().split()
# number_of_characters = []
#
# for word in l_text:
#     number_of_characters.append(len(word))
#
# print(max(number_of_characters))

print(max(list(len(word) for word in input().split())))
