# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# num = int(input('Введите число элементов: '))
# my_list = []
# sum = 0
# for i in range(1, num+1): # на 0 делить нельзя
#     my_list.append(round((1 + 1/i)**i, 2))
#     sum = sum + (1 + 1/i)**i

# print(f'Для n = {num} => {my_list}')
# print(f'Сумма элементов => {round(sum, 2)}')

# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.

num = int(input('Введите число элементов: '))
my_list = [round((1 + 1/i)**i, 2) for i in range(1, num+1)]
sum_elem = sum(my_list )
print(f'Для n = {num} => {my_list}')
print(f'Сумма элементов => {round(sum_elem, 2)}')