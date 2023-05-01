# Задание 3.
# 
# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
# 
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" исключение,
# придумайте как это сделать

words_list = ["attribute", "класс", "функция", "type"]

for word in words_list:

    try:
        b_word = bytes(word, 'ascii')
        print(f'{word} в байтовом представлении: {b_word}')

    except UnicodeEncodeError:
        print(f"{word}' невозможно записать в байтовом представлении в "
              f"кодировке ASCII", end="")
        b_word = bytes(word, 'utf-8')
        print(f", попробуйте записать в кодовых точках utf-8: {b_word}")