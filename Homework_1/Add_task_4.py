# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# Пример:
#
# 6 -> 1 4 1
#
# 24 -> 4 16 4
#
# 0 -> 10 40 10

crane_sum = int(input("Введите число журавликов: "))
if crane_sum % 6 == 0:
    Petya_serega_sum = crane_sum / 6
    Katya_sum = crane_sum / 6 * 4
    print(f"Петя и Сережа сделали по {int(Petya_serega_sum)} журавликов, а Катя сделала {int(Katya_sum)} журавликов")
elif crane_sum % 6 == 1:
    Petya_serega_sum = crane_sum // 6
    Katya_sum = crane_sum // 6 * 4 + 1
    print(f"Петя и Сережа сделали по {int(Petya_serega_sum)} журавликов, а Катя сделала {int(Katya_sum)} журавликов")
elif crane_sum % 6 == 2:
    Petya_serega_sum = crane_sum // 6
    Katya_sum = crane_sum // 6 * 4 + 2
    print(f"Петя и Сергеи сделали по {int(Petya_serega_sum)} журавликов, а Катя сделала {int(Katya_sum)} журавликов")
elif crane_sum % 6 == 3:
    Petya_serega_sum = crane_sum // 6
    Katya_sum = crane_sum // 6 * 4 + 3
    print(f"Петя и Сергеи сделали по {int(Petya_serega_sum)} журавликов, а Катя сделала {int(Katya_sum)} журавликов")
else:
    print("Если дети начинают работать вместе, то такое количество журавликов у них не выходит")