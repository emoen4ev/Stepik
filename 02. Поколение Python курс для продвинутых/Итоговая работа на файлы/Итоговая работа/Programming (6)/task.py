mapping_table = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*',
    'ы': 'y', 'ь': "'", 'э': 'je', 'ю': 'ju', 'я': 'ya',
}

file_name = 'cyrillic.txt'
# file_name = 'cyrillic_1.txt'

with open(file_name, 'rt', encoding='utf-8') as input_file, open('transliteration.txt', 'wt', encoding='utf-8') as output_file:
    for line in input_file:
        for ch in line:
            if ch.lower() in mapping_table:
                new_ch = (mapping_table[ch.lower()], (mapping_table[ch.lower()][0].upper() + mapping_table[ch.lower()][1:]))[ch.isupper()]
                line = line.replace(ch, new_ch)

        output_file.write(line)