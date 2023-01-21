# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

# number = int(input('Введите число элементов в списке: '))
# my_list = []
# for i in range(number):
#     my_list.append(randint(0, 5))
# print(my_list)

# new_list = []
# for i in range(len(my_list)):
#     if my_list[i] not in new_list:
#         new_list.append(my_list[i])
# print(new_list)


# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.

number = int(input('Введите число элементов в списке: '))
my_list = [randint(0, 5) for _ in range(number)]
print(my_list)

new_list = []
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i] not in new_list]
print(new_list)

