"""
Дополните приведенный ниже код, чтобы в переменной dt содержался объект типа datetime с датой и временем,
которые указаны в строке text.

Примечание. Дата, указанная в строке text, записана в формате DD.MM.YYYY, а время — в формате HH:MM.
"""

from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'

dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)