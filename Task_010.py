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