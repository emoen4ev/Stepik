p = int(input())  # въвеждане в минути
h = p // 60  # часове
m = (p - h * 60)  # минути
# print(p, "мин - это", h, "час", m, "минут.")
# print(f"{p} мин - это {h} час {m} минут")
print("{} мин - это {} час {} минут.".format(p, h, m))



