#Task 2:

# Получить с русской википедии список всех животных
# (Категория:Животные по алфавиту) и вывести количество животных
# на каждую букву алфавита.

import wikipediaapi


def print_alphabet_animals_count(lang, page):
    wiki = wikipediaapi.Wikipedia(language=lang)

    category = wiki.page(page)

    rus_animals = {}

    for cat_member in category.categorymembers.values():
        first_char = cat_member.title[0].upper()
        if 'А' <= first_char <= 'Я':
            if first_char in rus_animals:
                rus_animals[first_char] += 1
            else:
                rus_animals[first_char] = 1

    list_keys = list(rus_animals.keys())
    list_keys.sort()
    for key in list_keys:
        print(f'{key}: {rus_animals[key]}')


print_alphabet_animals_count(lang='ru', page='Категория:Животные_по_алфавиту')
