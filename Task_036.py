# Найти сумму чисел списка стоящих на нечетной позиции


# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.

import random

number = int(input('Введите число элементов в списке: '))
my_list = [random.randint(0, 5) for _ in range(number)]
print(my_list)
sun_odd_index = sum([value for index, value in enumerate(my_list) if index % 2 !=0])
sun_odd_index_1 = sum(list(map(lambda x: my_list[x] if x%2 == 1 else 0, list(range(len(my_list))))))
print(sun_odd_index)
print(sun_odd_index_1)