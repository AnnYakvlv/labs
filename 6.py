def count_box():
    countries = {"Бельгия": 'Брюссель', "Великобритания": 'Лондон', "Венесуэлла": 'Каракас', "Италия": 'Рим',
                 "Испания": 'Мадрид', "Россия": 'Москва', "Япония": 'Токио', "Франция": 'Париж', "Турция": 'Анкара',
                 "Южная Корея": 'Сеул', "США": 'Вашингтон', "Норвегия": 'Осло', "Непал": 'Катманду', "Монако": 'Монако',
                 "Аргентина": 'Буэнос-Айрес'}
    print(countries)
    c = input("Введите страну: ")
    print(countries[c])
    print(sorted(countries.items()))


def word_score():
    words = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    word = input("введите слово: ")
    sum = 0
    for i in word:
        sum += words[i.lower()]
    print("сумма: ", sum)


def chi_lg():
    student = {"Беликова": 'Нелли', "Васильев": 'Артем', "Гумерова": 'Эвелина',
        "Лыткин": 'Владимир', "Обрывалина": 'Валентина'}
    lang = {"Беликова": ['русский','английский'], "Васильев": ['французкий'],
            "Гумерова": ['японский','китайский'],
        "Лыткин": ['русский','корейский'], "Обрывалина": ['китайский', 'итальянский']}
    one_more = {}
    chinese = {}
    for key in lang:
        if len(lang[key]) > 1:
            one_more[key] = student[key]
        for i in lang[key]:
            if i == 'китайский':
                chinese[key] = student[key]
    print('\nСтуденты, знающие больше одного языка: ')
    for key in one_more:
        print(key, one_more[key])
    print('\nСтуденты, знающие китайский язык: ')
    for key in chinese:
        print(key, chinese[key])

count_box()
word_score()
chi_lg()