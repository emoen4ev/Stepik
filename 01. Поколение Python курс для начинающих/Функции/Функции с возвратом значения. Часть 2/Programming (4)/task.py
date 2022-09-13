# объявление функции
def is_one_away(word1, word2):
    counter = 0

    if len(word1) != len(word2):
        return False

    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            counter += 1

    if counter == 1:
        return True

    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))