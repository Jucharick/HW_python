# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

coordinateXA = int(input('Введите координату X точки A: '))
coordinateYA = int(input('Введите координату Y точки A: '))
coordinateXB = int(input('Введите координату X точки B: '))
coordinateYB = int(input('Введите координату Y точки B: '))

distance = math.sqrt((coordinateXA - coordinateXB)**2 + (coordinateYA - coordinateYB)**2)
print(round(distance, 2))


# вариант преподавателя
first = input('Введите координаты точки А через пробел: ').split(' ')
second = input('Введите координаты точки B через пробел: ').split() # split() по умолчанию ставит пробел

distance1 = (float(first[0]) - float(second[0]))**2 + (float(first[1]) - float(second[1]))**2 
print(f'Расстояние между точками А и В равно => {round(math.sqrt(distance1), 2)}')