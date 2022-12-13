s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange' \
    ' barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot' \
    ' currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon' \
    ' pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple' \
    ' barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit' \
    ' banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

s = s.split()

result = {}

for word in s:
    if word not in result:
        result[word] = s.count(word)

result = sorted(result.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])