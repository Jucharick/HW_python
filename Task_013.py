# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
from random import randint

num = int(input('Введите число элементов: '))
my_list = []

for i in range(num):
    my_list.append(i)
print(my_list)

for i in range(num):
    new_i = randint(0, num - 1)
    temp = my_list[i]
    my_list[i] = my_list[new_i]
    my_list[new_i] = temp

print(my_list)
