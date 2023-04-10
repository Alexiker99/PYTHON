# Задание 34 ###
#
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# Пример:
#
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
#
# Вывод:** Парам пам-пам  

class Song:

    def __init__(self, text):
        self.text = text

    def pooh_analiz(self):
        flag = True
        tmp = 0
        for frase in self.text.split(' '):
            count = 0
            small = frase.split('-')
            for word in small:
                for ch in word:
                    if ch in "ауоыиэяюёе":
                        count += 1
            if tmp == 0:
                tmp = count
            if tmp != count:
                flag = False
                break
        return "Парам пам-пам" if flag else "Пам парам"


obj = Song("пара-ра-рам рам-пам-папам па-ра-па-да")
print(obj.pooh_analiz())