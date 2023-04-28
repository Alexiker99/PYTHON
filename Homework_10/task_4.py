# Задание 4.
#
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции

words_list = ["разработка", "администрирование", "protocol", "standard"]

byte_list = [word.encode() for word in words_list]

for i, word in enumerate(byte_list):
    print(f"{words_list[i]} = {byte_list}")

decoded_array = [byte_word.decode() for byte_word in byte_list]

for word in decoded_array:
    print(word)
