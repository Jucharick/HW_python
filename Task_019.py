# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number = int(input('Введите число элементов в списке: '))
my_list = []
sum = 0
for i in range(number):
    my_list.append(int(input('Введите число: ')))
print(my_list)
for i in range(1, number, 2):
    sum = sum + my_list[i]
print(f'Сумма элементов списка, стоящих на позиции с нечетным индексом, => {sum}')