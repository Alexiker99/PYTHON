# Задача 28
# 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# Пример:
# 
# 2 2 <- 4

def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def get_sum(a, b):
    if b == 0:
        return a
    if b > 0:
        return get_sum(a + 1, b - 1)
    return get_sum(a - 1, b + 1)


def start_app():
    a = get_int_from_user('Введите 1 слагаемое: ')
    b = get_int_from_user('Введите 2 слагаемое: ')
    if a is not None and b is not None:
        print(f'Результат a + b = {get_sum(a, b)}')
    else:
        print('Ошибка, повторите')


if __name__ == "__main__":
    start_app()