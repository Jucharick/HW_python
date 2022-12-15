# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


coordinate = int(input('Введите номер четверти плоскости: '))
if coordinate == 1:
    print('x > 0; y > 0')
elif coordinate == 2:
    print('x < 0; y > 0')
elif coordinate == 3:
    print('x < 0; y < 0')
elif coordinate == 4:
    print('x > 0; y < 0')
else:
    print('Вы ввели некоррекное значение')