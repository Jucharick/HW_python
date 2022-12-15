# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30    -> 4
# - x=2; y=4       -> 1
# - x=-34; y=-30   -> 3


coordinateX = int(input('Введите координату X: '))
coordinateY = int(input('Введите координату Y: '))
if coordinateX > 0 and coordinateY > 0:
    print('Точка находится в 1 четверти плоскости')
elif coordinateX < 0 and coordinateY > 0:
    print('Точка находится в 2 четверти плоскости')
elif coordinateX < 0 and coordinateY < 0:
    print('Точка находится в 3 четверти плоскости')
elif coordinateX > 0 and coordinateY < 0:
    print('Точка находится в 4 четверти плоскости')
elif coordinateX == 0 and coordinateY != 0:
    print('Точка находится на оси абсцисс')
elif coordinateX != 0 and coordinateY == 0:
    print('Точка находится на оси ординат')
else:
    print('Точка находится в начале координат')