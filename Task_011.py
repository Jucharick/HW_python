# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# математика

from decimal import Decimal # библиотека позволяет работать с плавающими точками без 0.00000000000000006
number = abs(Decimal(input('Введите дробное число: '))) # abs - модуль
quantity = 0
while  number % 10 != 0: # последний лишний ноль не отразится на сумме цифр
    number*=10
while number > 0:
    quantity = quantity + int(number) % 10
    number = int( number / 10)
print(f'Сумма цифр вещественного числа => {quantity}')


# через список подстрок

num = (input('Введите дробное число: '))
count = 0
if num[0] == '-':
    num = num [1:len(num)] # если число отрицательное => убираю у него первый символ

list = num.split('.')
if len(list) <= 2: # проверяю, что пользователь ввел не более одной точки
    for i in range(len(list)):
        # print (list[i])
        for j in range(len(list[i])): # иду по каждой подстроке i по каждому элементу j
            count = count + int(list[i][j])
    print(f'Сумма цифр вещественного числа => {count}')
else:
    print('Вы ввели не число')