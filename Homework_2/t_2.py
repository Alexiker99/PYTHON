# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# етя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.  
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


sum_value = int(input("Сумма 2-ух натуральных чисел: "))
multiplication_value = int(input("Произведение 2-ух натуральных чисел: "))
discriminant = sum_value**2 - 4 * multiplication_value
if discriminant > 0:
    var_y = (sum_value + discriminant**0.5) / 2
    var_x = sum_value - var_y
    if multiplication_value == var_x * var_y:
        print(var_x, var_y)
    else:
        print("натуральных решений нет")
elif discriminant == 0:
    var_y = sum_value / 2
    var_x = sum_value - var_y
    print(var_x, var_y)
elif discriminant < 0:
    print("решений нет")