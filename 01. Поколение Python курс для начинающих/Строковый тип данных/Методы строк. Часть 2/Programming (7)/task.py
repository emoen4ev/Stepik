text = input()

first_index = text.find("h")
last_index = text.rfind("h")
f_cut = text[first_index:last_index + 1]
the_end = text.replace(f_cut, "")

print(the_end)