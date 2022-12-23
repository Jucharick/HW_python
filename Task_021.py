# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import decimal

number = int(input('Введите число элементов в списке: '))
my_list = []
for i in range(number):
    amount = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), amount))
print(my_list)

min = 0
max = 0
for i in range(len(my_list)):
    if my_list[i] != int(my_list[i]):
        part = my_list[i] - int(my_list[i])
        print(part)
        if part > max:
            max = part
        if part < min:
            min = part

print(max)
print(min)
