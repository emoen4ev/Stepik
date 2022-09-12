text = input()

lower_text = text.lower()

a = lower_text.count("а")
g = lower_text.count("г")
c = lower_text.count("ц")
t = lower_text.count("т")

print("Аденин:", a)
print("Гуанин:", g)
print("Цитозин:", c)
print("Тимин:", t)
