# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.

import math

first = [int(input('Введите координаты точки А: ')) for _ in range(2) ]
second = [int(input('Введите координаты точки B: ')) for _ in range(2) ]

res = round(sum([(elem[1] - elem[0])**2 for elem in zip(first, second)])**0.5 , 2)
print(f'Расстояние между точками А и В равно => {res}')
