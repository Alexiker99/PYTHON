# Задание 2.
# 
# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.
# 
# Подсказки:
# --- b'class' - используйте маркировку b''
# --- используйте списки и циклы, не дублируйте функции

words_list = ['class', 'function', 'method']
byte_list = [bytes(word, 'utf-8') for word in words_list]

for word in byte_list:
    print(f'{word}.Тип данных: {type(word)} Длина переменной: {len(word)}')