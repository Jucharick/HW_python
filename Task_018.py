# Реализуйте алгоритм перемешивания списка.

# SHUFFLE
import random

number = int(input('Введите число элементов: '))
my_list = []

for i in range(number):
    my_list.append(i)
print(my_list)
random.shuffle(my_list)
print(my_list)


# через замену местами 
from random import randint

num = int(input('Введите число элементов: '))
my_list1 = []
for i in range(num):
    my_list1.append(i)
print(my_list1)
for i in range(num):
    new_i = randint(0, num - 1)
    temp = my_list1[i]
    my_list1[i] = my_list1[new_i]
    my_list1[new_i] = temp
print(my_list1)
