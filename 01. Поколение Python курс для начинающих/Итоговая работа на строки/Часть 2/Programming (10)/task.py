text = input()

text_start = text[:text.find("h") + 1]
text_middle = ""
text_final = text[text.rfind("h"):]

for i in range(text.rfind("h") - 1, text.find("h"), - 1):
    text_middle += text[i]

print(text_start + text_middle + text_final, end="")