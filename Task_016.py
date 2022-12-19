# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06


num = int(input('Введите число элементов: '))
my_list = []
sum = 0
for n in range(1, num+1): # на 0 делить нельзя
    my_list.append(round((1 + 1/n)**n, 2))
    sum = sum + (1 + 1/n)**n
print(f'Для n={num}  => (', end = ' ')
for i in range(len(my_list)):
    print(f'{i+1}: {my_list[i]} ', end = ' ')
print(')')
print(f'Сумма элементов => {round(sum, 2)}')