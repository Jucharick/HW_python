# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Введите число элементов: '))
# my_list = []
# number = 1
# for i in range(0, num):
#     number = number*(i+1)
#     my_list.append(number)
# print(f'Для n = {num} => {my_list}')


# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension.


def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x- 1)

my_list = [f(i) for i in range(1, num+1)] 
print(f'Для n = {num} => {my_list}')