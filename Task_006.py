# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

dayWeek = int(input('Введите день недели. Например 1 -> Monday: '))
if 1 <= dayWeek <= 5:
    print('нет, еще не выходной')
elif 6 <= dayWeek <= 7:
    print('да, выходной')
else:
    print('вы ввели некорректное значение')