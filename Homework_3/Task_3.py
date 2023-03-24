# Задание №3:
#
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
#
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# mail: jackie@gmail.com, телефон: 01005321456
'''''
name = input('Введите Имя')
surname = input('Введите Фамилию')
year = int(input('Введите год рождения'))
city = input('Введите Город')
email = input('Введите @email')
telephone = input('Введите телефон')
'''
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Леонтьев', name = 'Алексей', year = '1995', city = 'Сызрань', email = 'error@mail.ru', telephone = '8-800-555-35-35'))