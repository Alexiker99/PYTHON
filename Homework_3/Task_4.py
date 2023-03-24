# Задание №4:
#
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
#
# - используя функцию sort()
# - без функции sort()

# 1 без функции sort()
'''''
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат - {my_func(int(input("Введите 1 аргумент: ")), 
    int(input("Введите 2 аргумент: ")), int(input("Введите 3 аргумент: ")))}')
'''
# используя функцию sort()

def my_fun2(arg1, arg2, arg3):
    list_1 = sorted([arg1, arg2, arg3])
    res = list_1[1] + list_1[2]
    print(res)