# Найти сумму чисел списка стоящих на нечетной позиции


import random

number = int(input('Введите число элементов в списке: '))
my_list = [random.randint(0, 5) for _ in range(number)]
print(my_list)
sun_odd_index = sum([my_list[i] for i in range(len(my_list)) if i % 2 !=0])
print(sun_odd_index)