# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Введите число элементов: '))
my_list = []
number = 1
for i in range(0, num):
    number = number*(i+1)
    my_list.append(number)
print(f'Для n = {num} => {my_list}')
