# Задача 2: Найдите сумму цифр трехзначного числа.
#
# Пример:
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input("Введите трёхзначное число: "))
if 99 < a < 1000:
    result = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2])
    print(f"Сумма чисел трёхзначного числа: {result}")
else:
    print("Прочтите условия еще раз ")