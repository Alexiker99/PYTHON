# Задание №2:
#
# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
#
# Пример:
#
# Введите первое число: 10
# 
# Введите второе число: 0
# 
# Вы что? Пытаетесь делить на 0!
# 
# Process finished with exit code 0
# 
# Пример:
#
# Введите первое число: 10
#
# Введите второе число: 10



def div(*args):

    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка в значении '
    except ZeroDivisionError:
        return "В делителе ошибка! Вы не можете делить на ноль! "

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Ошибка в числе! Делимое не может быть нулевым")
    '''


print(f'Результат 10{div()}')