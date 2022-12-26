# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число N: '))
list_nums = []
divider = 1
for i in range(num):
    divider = divider + 1
    if int(num) % divider == 0:
        list_nums.append(divider)
        num //= divider
        divider = 1
print(f'список простых множителей числа N => {list_nums}')