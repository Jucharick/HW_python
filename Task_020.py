# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
from random import randint

# number = int(input('Введите число элементов в списке: '))
# my_list = []
# for i in range(number):
#     my_list.append(randint(0, 7))
# res = []
# for i in range(math.ceil((number/2))): # math.ceil() округление в большую сторону
#     res.append(my_list[i]*my_list[number - 1 - i])
# print(f'{my_list}  =>  {res}')

number = int(input('Введите число элементов в списке: '))
my_list = [randint(0, 7) for _ in range(number)]
res = [my_list[i]*my_list[number - 1 - i] for i in range(math.ceil((number/2)))]

print(f'{my_list}  =>  {res}')