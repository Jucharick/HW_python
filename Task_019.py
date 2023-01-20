# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number = int(input('Введите число элементов в списке: '))

# sum = 0

# my_list = []
# for i in range(number):
#     my_list.append(int(input('Введите число: ')))
# print(my_list)
# for i in range(1, number, 2):
#     sum = sum + my_list[i]
# print(f'Сумма элементов списка, стоящих на позиции с нечетным индексом, => {sum}')


# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.

my_list = [int(input('Введите число: ')) for _ in range(number) ]
print(my_list)
sun_odd_index = sum([my_list[i] for i in range(len(my_list)) if i % 2 !=0])
print(sun_odd_index)