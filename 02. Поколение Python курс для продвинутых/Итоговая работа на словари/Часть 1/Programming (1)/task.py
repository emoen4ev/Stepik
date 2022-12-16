emails = {
    'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
    'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
    'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
    'yandex.ru': ['surface', 'google'],
    'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
    'mail.ru': ['angel.down', 'joanne', 'the.fame.moster'],
}

result = []

for k, v in emails.items():
    current_list = [el + '@' + k for el in sorted(v)]
    result.extend(current_list)

result.sort()

for item in result:
    print(item)