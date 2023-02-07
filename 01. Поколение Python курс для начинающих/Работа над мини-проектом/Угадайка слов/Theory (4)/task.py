from random import choice


def get_word():
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        ''' 
           -------- 
           |      | 
           |      O 
           |     \\|/ 
           |      | 
           |     / \\
          --- 
        ''',
        # голова, торс, обе руки, одна нога
        ''' 
           -------- 
           |      | 
           |      O 
           |     \\|/ 
           |      | 
           |     /  
          --- 
        ''',
        # голова, торс, обе руки
        ''' 
           -------- 
           |      | 
           |      O 
           |     \\|/ 
           |      | 
           |       
          --- 
        ''',
        # голова, торс и одна рука
        ''' 
           -------- 
           |      | 
           |      O 
           |     \\| 
           |      | 
           |      
          --- 
        ''',
        # голова и торс
        ''' 
           -------- 
           |      | 
           |      O 
           |      | 
           |      | 
           |      
          --- 
        ''',
        # голова
        ''' 
           -------- 
           |      | 
           |      O 
           |     
           |       
           |      
          --- 
        ''',
        # начальное состояние
        ''' 
           -------- 
           |      | 
           |       
           |     
           |       
           |      
          --- 
        '''
    ]
    return stages[tries]


def validate_input_data(w_completion, f_attempts, r_errors):
    input_data = ''
    is_valid_input = False
    while not is_valid_input:
        print()
        print(f'Вы сделали {f_attempts} ошибки до сих пор. Вы имеете право на еще {r_errors} ошибки.')
        print()
        print('Слово, которое нужно угадать: ', w_completion)
        print()
        input_data = input('Введите букву или слово: ').upper()
        print()
        if not input_data:
            print('Вы ничего не ввели ...')
            continue
        elif len(input_data) == 1:
            if not validate_is_letters_only(input_data):
                print('Это не буква ... Неверный ввод ...')
                continue
            if validate_is_already_used(input_data):
                print('Вы уже использовали эту букву ...')
                continue
            guessed_letters.append(input_data)
        else:
            if not validate_is_letters_only(input_data):
                print('Ваш ввод содержит символы, отличные от букв... Неверный ввод...')
                continue
            if validate_is_already_used(input_data):
                print('Вы уже использовали это слово ...')
                continue
            guessed_words.append(input_data)
        is_valid_input = True
    return input_data


def validate_is_letters_only(input_characters):
    is_all_letters = True
    for character in input_characters:
        if not character.isalpha():
            is_all_letters = False
            break
    return is_all_letters


def validate_is_already_used(input_characters):
    is_used = False
    if input_characters in guessed_letters or input_characters in guessed_words:
        is_used = True
    return is_used


def get_new_word_completion(current_char, word_to_know, output_word):
    for i in range(len(word_to_know)):
        if word_to_know[i] == current_char:
            output_word = output_word[:i] + current_char + output_word[i + 1:]
    return output_word


def play():
    word = get_word()
    possible_errors = 6
    remaining_errors = possible_errors
    failed_attempts = 0
    guessed = False
    word_completion = '_' * len(word)

    print()
    print('Давайте играть в угадайку слов!')
    print(display_hangman(remaining_errors))
    print(word)

    while True:
        input_data = validate_input_data(word_completion, failed_attempts, remaining_errors)
        if input_data == word:
            print(f'Молодец, ты победил ... !\nУгадал слово {word} с {failed_attempts} ошибками.')
            guessed = True
            break
        elif len(input_data) == 1 and input_data in word:
            print('Отлично, эта буква содержится в слове ...')
            word_completion = get_new_word_completion(input_data, word, word_completion)
            continue
        elif len(input_data) == 1 and input_data not in word:
            print('Этой буквы нет в слове ... ')
        elif len(input_data) > 1 and input_data != word:
            print('Вы не угадали, это не то слово ...')
        failed_attempts += 1
        remaining_errors = possible_errors - failed_attempts
        if remaining_errors < 1:
            print(display_hangman(remaining_errors))
            print(f'К сожалению проиграл игру ... !\nСлово, которое нужно было угадать, было: {word}.\n')
            break
        print(display_hangman(remaining_errors))
        continue

    while True:
        print()
        answer = input('Хочешь еще одну игру ...?   (да/нет)\n')
        if answer[0] in 'дДdDyY':
            play()
        elif answer[0] in 'нНnN':
            print('\nБыло приятно играть вместе ... ! До скорого ... !')
            quit()
        else:
            print('Я не понимаю этот ответ ... ? Я ожидаю <да> или <нет> в качестве ответа...?')
            continue


guessed_letters = []
guessed_words = []

word_list = [
    'год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
    'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
    'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода',
    'отец', 'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон',
    'война', 'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область',
    'статья', 'число', 'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие',
    'средство', 'начало', 'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица',
    'вечер', 'качество', 'мысль', 'дорога', 'мать', 'действие', 'месяц', 'государство', 'язык', 'любовь',
    'взгляд', 'мама', 'век', 'школа', 'цель', 'общество', 'деятельность', 'организация', 'президент',
    'комната', 'порядок', 'момент', 'театр', 'письмо', 'утро', 'помощь', 'ситуация', 'роль', 'рубль', 'смысл',
    'состояние', 'квартира', 'орган', 'внимание', 'тело', 'труд', 'сын', 'мера', 'смерть', 'рынок',
    'программа', 'задача', 'предприятие', 'окно', 'разговор', 'правительство', 'семья', 'производство',
    'информация', 'положение', 'центр', 'ответ', 'муж', 'автор', 'стена', 'интерес', 'федерация', 'правило',
    'управление', 'мужчина', 'идея', 'партия', 'совет', 'счет', 'сердце', 'движение', 'вещь', 'материал',
    'неделя', 'чувство', 'глава', 'наука', 'ряд', 'газета', 'причина', 'плечо', 'цена', 'план', 'речь',
    'точка', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ', 'институт', 'ход', 'проект',
    'встреча', 'директор', 'срок', 'палец', 'опыт', 'служба', 'судьба', 'девушка', 'очередь', 'лес', 'состав',
    'член', 'количество', 'событие', 'объект', 'зал', 'создание', 'значение', 'период', 'шаг', 'брат',
    'искусство', 'структура', 'номер', 'пример', 'исследование', 'гражданин', 'игра', 'начальник', 'рост',
    'тема', 'принцип', 'метод', 'тип', 'фильм', 'край', 'гость', 'воздух', 'характер', 'борьба',
    'использование', 'размер', 'образование', 'мальчик', 'кровь', 'район', 'небо', 'армия', 'класс',
    'представитель', 'участие', 'девочка', 'политика', 'герой', 'картина', 'доллар', 'спина', 'территория',
    'пол', 'поле', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'банк', 'сцена', 'население',
    'большинство', 'музыка', 'правда', 'свобода', 'память', 'команда', 'союз', 'врач', 'договор', 'дерево',
    'факт', 'хозяин', 'природа', 'угол', 'телефон', 'позиция', 'двор', 'писатель', 'самолет', 'объем', 'род',
    'солнце', 'вера', 'берег', 'спектакль', 'фирма', 'способ', 'завод', 'цвет', 'журнал', 'руководитель',
    'специалист', 'оценка', 'регион', 'песня', 'процент', 'родитель', 'море', 'требование', 'основание',
    'половина', 'роман', 'круг', 'анализ', 'стихи', 'автомобиль', 'экономика', 'литература', 'бумага', 'поэт',
    'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр', 'граница', 'дух', 'модель', 'операция',
    'пара', 'сон', 'название', 'ум', 'повод', 'старик', 'миллион', 'успех', 'счастье', 'ребята', 'кабинет',
    'магазин', 'пространство', 'выход', 'удар', 'база', 'знание', 'текст', 'защита', 'руководство', 'площадь',
    'сознание', 'возраст', 'участник', 'участок', 'пункт', 'линия', 'желание', 'папа', 'доктор', 'губа',
    'дочь', 'среда', 'председатель', 'представление', 'солдат', 'художник', 'волос', 'оружие', 'соответствие',
    'ветер', 'парень', 'зрение', 'генерал', 'огонь', 'понятие', 'строительство', 'ухо', 'грудь', 'нос',
    'страх', 'услуга', 'содержание', 'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сад',
    'сотрудник', 'лето', 'курс', 'предложение', 'рот', 'технология', 'реформа', 'отсутствие', 'собака',
    'камень', 'будущее', 'рассказ', 'контроль', 'река', 'продукция', 'сумма', 'техника', 'здание', 'сфера',
    'необходимость', 'фонд', 'подготовка', 'лист', 'республика', 'хозяйство', 'воля', 'бюджет', 'снег',
    'деревня', 'мужик', 'элемент', 'обстоятельство', 'немец', 'победа', 'источник', 'звезда', 'выбор', 'масса',
    'итог', 'сестра', 'практика', 'проведение', 'карман', 'слава', 'кухня', 'определение', 'функция', 'войско',
    'комиссия', 'применение', 'капитан', 'работник', 'обеспечение', 'офицер', 'фамилия', 'предел', 'выборы',
    'ученый', 'бутылка', 'бой', 'теория', 'зона', 'отдел', 'зуб', 'разработка', 'личность', 'гора', 'товар',
    'метр', 'праздник', 'влияние', 'читатель', 'удовольствие', 'актер', 'слеза', 'ответственность', 'учитель',
    'акт', 'боль', 'множество', 'особенность', 'показатель', 'корабль', 'звук', 'впечатление', 'частность',
    'детство', 'вывод', 'профессор', 'доля', 'норма', 'прошлое', 'командир', 'коридор', 'поддержка', 'рамка',
    'враг', 'этап', 'черт', 'дед', 'собрание', 'прием', 'болезнь', 'клетка', 'кожа', 'заявление', 'попытка',
    'сравнение', 'расчет', 'депутат', 'комитет', 'знак', 'дядя', 'учет', 'хлеб', 'чай', 'режим', 'целое',
    'вирус', 'выражение', 'здоровье', 'зима', 'десяток', 'глубина', 'сеть', 'студент', 'секунда', 'скорость',
    'поиск', 'суть', 'налог', 'ошибка', 'доход', 'режиссер', 'поверхность', 'ощущение', 'карта', 'клуб',
    'станция', 'революция', 'колено', 'министерство', 'стекло', 'этаж', 'высота', 'бабушка', 'трубка', 'газ',
    'мастер', 'поведение', 'столица', 'механизм', 'передача', 'способность', 'подход', 'энергия',
    'существование', 'исполнение', 'кино', 'сожаление', 'заместитель', 'ресурс', 'акция', 'рождение',
    'администрация', 'стоимость', 'улыбка', 'артист', 'сосед', 'фраза', 'фигура', 'субъект', 'реакция',
    'список', 'фотография', 'журналист', 'май', 'нарушение', 'заседание', 'толпа', 'больница', 'существо',
    'свойство', 'долг', 'поколение', 'животное', 'схема', 'усилие', 'отличие', 'остров', 'противник', 'волна',
    'реализация', 'страница', 'формирование', 'житель', 'красота', 'птица', 'растение', 'тень', 'явление',
    'храм', 'запах', 'водка', 'наличие', 'ужас', 'одежда', 'кресло', 'больной', 'поезд', 'университет',
    'традиция', 'адрес', 'декабрь', 'ладонь', 'сведение', 'цветок', 'лидер', 'октябрь', 'занятие', 'сентябрь',
    'помещение', 'январь', 'зритель', 'редакция', 'стиль', 'весна', 'фактор', 'август', 'известие',
    'зависимость', 'охрана', 'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция',
    'переход', 'эпоха', 'запад', 'произведение', 'родина', 'собственность', 'тайна', 'трава', 'лагерь',
    'имущество', 'кровать', 'аппарат', 'середина', 'март', 'клиент', 'дама', 'фронт', 'отрасль', 'стул',
    'беседа', 'законодательство', 'продажа', 'повышение', 'музей', 'след', 'полковник', 'сомнение',
    'понимание', 'апрель', 'князь', 'рыба', 'дума', 'кодекс', 'сутки', 'чудо', 'шея', 'судья', 'крыша',
    'настроение', 'поток', 'должность', 'преступление', 'мозг', 'честь', 'пост', 'еврей', 'июнь', 'сотня',
    'дождь', 'лестница', 'дача', 'установка', 'появление', 'получение', 'образец', 'труба', 'главное', 'осень',
    'костюм', 'баба', 'ценность', 'обязанность', 'пьеса', 'таблица', 'вино', 'воспоминание', 'лошадь',
    'коллега', 'организм', 'ученик', 'учреждение', 'открытие', 'том', 'черта', 'характеристика', 'выполнение',
    'оборона', 'выступление', 'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан',
    'километр', 'спор', 'вкус', 'признак', 'промышленность', 'американец', 'лоб', 'заключение', 'восток',
    'исключение', 'ключ', 'постановление', 'слой', 'бок', 'июль', 'перевод', 'секретарь', 'кусок', 'слух',
    'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина', 'зарплата',
    'билет', 'подарок', 'тюрьма', 'ящик', 'конкурс', 'книжка', 'изучение', 'просьба', 'царь', 'публика',
    'смех', 'сообщение', 'угроза', 'беда', 'блок', 'достижение', 'назначение', 'реклама', 'портрет', 'масло',
    'стакан', 'урок', 'часы', 'крик', 'творчество', 'телевизор', 'инструмент', 'концепция', 'лейтенант',
    'экран', 'дно', 'реальность', 'канал', 'мясо', 'знакомый', 'щека', 'конфликт', 'переговоры', 'запись',
    'вагон', 'площадка', 'последствие', 'сотрудничество', 'зеркало', 'тон', 'академия', 'палата',
    'потребность', 'ноябрь', 'увеличение', 'дурак', 'поездка', 'обед', 'потеря', 'февраль', 'мероприятие',
    'парк', 'принятие', 'устройство', 'вещество', 'категория', 'сезон', 'гостиница', 'издание', 'объединение',
    'темнота', 'человечество', 'колесо', 'опасность', 'разрешение', 'воздействие', 'коллектив', 'камера',
    'запас', 'следствие', 'длина', 'крыло', 'округ', 'фон', 'кандидат', 'родственник', 'давление',
    'присутствие', 'взаимодействие', 'доска', 'партнер', 'двигатель', 'шум', 'достоинство', 'грех', 'нож',
    'полёт', 'страсть', 'испытание', 'истина', 'оплата', 'разница', 'водитель', 'пакет', 'снижение', 'формула',
    'живот', 'капитал', 'мост', 'новость', 'эффект', 'вход', 'губернатор', 'доклад', 'смена', 'убийство',
    'эксперт', 'автобус', 'платье', 'кадр', 'тетя', 'общение', 'психология', 'лев', 'порог', 'проверка',
    'процедура', 'рабочий', 'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение',
    'буква', 'доказательство', 'признание', 'постель', 'штаб', 'владелец', 'компьютер', 'инженер', 'старуха',
    'лодка', 'ракета', 'серия', 'шутка', 'вершина', 'выпуск', 'кулак', 'лед', 'торговля', 'нефть', 'молодежь',
    'цифра', 'корпус', 'недостаток', 'сапог', 'сущность', 'талант', 'эффективность', 'кофе', 'полоса',
    'основное', 'рассмотрение', 'сбор', 'штат', 'следователь', 'жилье', 'мешок', 'описание', 'куст', 'отказ',
    'замок', 'редактор', 'дворец', 'забота', 'пиво', 'диван', 'столик', 'эксперимент', 'печать', 'кольцо',
    'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'добро', 'дружба', 'покой', 'риск',
    'окончание', 'дым', 'брак', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кость', 'спорт',
    'кредит', 'господь', 'майор', 'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'отдых',
    'ручка', 'металл', 'молоко', 'прокурор', 'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние',
    'мечта', 'село', 'еда', 'зло', 'подразделение', 'сюжет', 'рубеж', 'сигнал', 'атмосфера', 'крест', 'вес',
    'взрыв', 'контакт', 'сигарета', 'восторг', 'золото', 'почва', 'премия', 'король', 'подъезд', 'шанс',
    'автомат', 'заказ', 'мальчишка', 'очки', 'миг', 'штука', 'чтение', 'поселок', 'свидетель', 'ставка',
    'сумка', 'удивление', 'хвост', 'песок', 'поворот', 'возвращение', 'мгновение', 'статус', 'озеро', 'строй',
    'параметр', 'сказка', 'тенденция', 'вина', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'дочка',
    'танец', 'эксплуатация', 'коммунист', 'пенсия', 'приятель', 'объяснение', 'набор', 'производитель', 'пыль',
    'философия', 'мощность', 'обязательство', 'уход', 'горло', 'кризис', 'указание', 'плата', 'яблоко',
    'препарат', 'действительность', 'москвич', 'остаток', 'изображение', 'сделка', 'сочинение', 'покупатель',
    'танк', 'затрата', 'строка', 'единица',
]

play()