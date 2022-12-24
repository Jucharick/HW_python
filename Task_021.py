# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from decimal import Decimal

number = int(input('Введите число элементов в списке: '))
my_list = []
for i in range(number):
    amount = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), amount))
print(my_list)

new_list = []
for i in range(len(my_list)):
    if my_list[i] != int(my_list[i]):
        part = round(my_list[i]- int(my_list[i]), 3) # не знаю как корректно округлить дробную часть, взяла максимальное из amount
        new_list.append(part)
print(f'{my_list}  =>  {round((max(new_list) - min(new_list)), 3)}')


# не используя методы max() и min()
max = new_list[0]
min = new_list[0]
for i in range(len(new_list)):
    if new_list[i] < min:
        min = new_list[i]
    if new_list[i] > max:
        max = new_list[i]
print(f'{my_list}  =>  {round((max - min), 3)}')