# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
from random import randint

num = int(input('Введите число элементов: '))
my_list = []

for i in range(num):
    my_list.append(i)
print(my_list)

for i in range(num):
    new_i = randint(0, num - 1)
    # temp = my_list[i]
    # my_list[i] = my_list[new_i]
    # my_list[new_i] = temp
    my_list[i], my_list[new_i] = my_list[new_i], my_list[i] # в пайтон можно делать замену таким образом, не используя temp как в C#
print(my_list)


# вариант преподавателя
def my_shuffle(my_list: list):
    
    new_list = []
    while len(my_list) > 0:
        ni = randint(0, (len(my_list) - 1)) 
        new_list.append(my_list.pop(ni))
    return new_list

print('Вариант преподавателя')
print(my_list)
print(my_shuffle(my_list))