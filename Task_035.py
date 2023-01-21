# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# Ускоренная об
import math

first = [int(input('Введите координаты точки А: ')) for _ in range(2) ]
second = [int(input('Введите координаты точки B: ')) for _ in range(2) ]

distance1 = (float(first[0]) - float(second[0]))**2 + (float(first[1]) - float(second[1]))**2 
print(f'Расстояние между точками А и В равно => {round(math.sqrt(distance1), 2)}')