# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


num = (input('Введите дробное число: '))

count = 0
if :
    list = num.split('.')
    for i in range(len(list)):
        print(list[i])
        for j in range(len(list[i])):
            count = count + int(list[i][j])
    print(f'Сумма цифр вещественного числа => {count}')
else:
    print('Вы ввели не вещественное число')