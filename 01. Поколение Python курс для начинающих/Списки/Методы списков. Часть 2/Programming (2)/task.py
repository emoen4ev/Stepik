text = input()

text_lowercase = text.lower()
list_text_lowercase = text_lowercase.split()

counter_a = list_text_lowercase.count('a')
counter_an = list_text_lowercase.count('an')
counter_the = list_text_lowercase.count('the')

sum_counters = counter_a + counter_an + counter_the

print(f"Общее количество артиклей: {sum_counters}")
