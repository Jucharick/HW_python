# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

number = int(input('Введите число элементов в списке: '))
my_list = []
for i in range(number):
    my_list.append(random.randint(0, 5))
print(my_list)

new_list = []
for i in range(len(my_list)):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
print(new_list)