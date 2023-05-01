# Задание 1.
#
# Каждое из слов «разработка», «сокет», «декоратор» представить
# в буквенном формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать
# в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
# и также проверить тип и содержимое переменных.
# 
# *Попытайтесь получить кодовые точки без онлайн-конвертера!
# без хардкода!
#
# Подсказки:
# --- 'разработка' - буквенный формат
# --- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
#--- используйте списки и циклы, не дублируйте функции

import chardet

words_list = ['разработка', 'сокет', 'декоратор']


byte_list = [word.encode() for word in words_list]


code_points = []
for word in words_list:
    code_word = ''
    for letter in word:
        code_word += f"\\u{ord(letter):04x}"
    code_points.append(code_word)


for i, word in enumerate(words_list):
    word_type = chardet.detect(byte_list[i])['encoding']
    print(f'{word}: {type(word)} в виде кодовых точек: '
          f'{type(code_points[i])}, '
          f'{code_points[i]}\n')
