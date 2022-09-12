text = input()

counter_max = 0
char_max = ""

for c in text:
    counter_curr = text.count(c)
    if counter_curr >= counter_max:
        counter_max = counter_curr
        char_max = c

print(char_max)

# --------------------------------------------------

# text = input()
#
# counter_max = 0
# char_max = ""
#
# for c in text:
#     counter_curr = 0
#     for k in text:
#         if c == k:
#             counter_curr += 1
#             if counter_curr >= counter_max:
#                 counter_max = counter_curr
#                 char_max = c
#
# print(char_max)