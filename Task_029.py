# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]


import random


# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# множители
def Create_dict(k: int) -> dict:
    equation = {}
    for i in range(k, -1, -1): # до степени 0 => граница -1 не включается
        equation[i] = random.randint(-4, 3)
    return equation

# создается строка - многочлен
def Create_string(equation: dict) -> str:
    eq_str = ''
    for k, v in equation.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
        if v > 0 and k == 1:
            eq_str += f'{v}*x + '
        elif v > 0 and k == 0:
            eq_str += f'{v} + '
        elif v < 0 and k == 1:
            eq_str += f'{v}*x - '
        elif v < 0 and k == 0:
            eq_str += f'{abs(v)} - '
        elif v < 0:
            eq_str += f'{v}*x**{k} - '
        elif v == 1 and k == 1:
            eq_str += f'*x + '
        elif v == 0:
            eq_str += f''
        else:
            eq_str += f'{v}*x**{k} + '
    else:
        eq_str =  eq_str[:-3] # вконце строки отрезаем 3 сивола  => пробел плюс пробел
        eq_str += f' = 0'
    return eq_str

# запись в файл
def Write_file(str: str, name_file: str):
    data = open(name_file, 'w') # открытие на запись
    data.writelines(str)
    data.close()


# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# чтение из файла
def Read_file(name_file: str) -> str:
    str = ''
    data = open(name_file, 'r') # открытие на чтение 
    for line in data:
        str += line
    data.close()
    return str

# преобразование строки в словарь
def Create_dict_polynomial(new_string: str) -> dict:
    equation = {}
    polynomial = new_string.replace(' ', '').replace('=0', ''). replace('+', ' ').replace('-', ' -').split()
    len_str = len(polynomial) - 1
    for i in range(len_str, -1, -1):
        if polynomial[len_str - i].startswith('x'):
            equation[i] = polynomial[len_str - i]
        else: 
            equation[i] = int(polynomial[len_str - i].split('*')[0])
    return equation

# сумма значений двух словарей => сумма множителей перед Х
def Sum_of_polynomials(dict_1: dict, dict_2: dict) -> dict:
    sum_pol = {}
    if len(dict_1) > len(dict_2):
        for k, v in dict_1.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
            if k in dict_1 and k not in dict_2:
                sum_pol[k] = dict_1.get(k, v)
            # elif v < 0:
            #     sum_pol[k] = dict_1.get(k, v) - dict_2.get(k, v)
            else:
                sum_pol[k] = dict_1.get(k, v) + dict_2.get(k, v)
    if len(dict_1) <= len(dict_2):
        for k, v in dict_2.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
            if k in dict_2 and k not in dict_1:
                sum_pol[k] = dict_2.get(k, v)
            # elif v < 0:
            #     sum_pol[k] = dict_1.get(k, v) - dict_2.get(k, v)
            else:
                sum_pol[k] = dict_1.get(k, v) + dict_2.get(k, v)
    return sum_pol


# создание двух многочленов и запись в два файла
k_1 = int(input('Введите максимальную степень для многочлена: '))
equation_1 = Create_dict(k_1)
print(equation_1)
eq_str_1 = Create_string(equation_1)
print(eq_str_1)
Write_file(eq_str_1,'equation_1.txt')

k_2 = int(input('Введите максимальную степень для второго многочлена: '))
equation_2 = Create_dict(k_2)
print(equation_2)
eq_str_2 = Create_string(equation_2)
print(eq_str_2)
Write_file(eq_str_2, 'equation_2.txt')


# чтение двух многочленов из двух файлов, суммирование словарей, запись суммы в файл
print('Первый многочлен')
eq_read_1 = Read_file('equation_1.txt')
print(eq_read_1)
polynomial_1 = Create_dict_polynomial(eq_read_1)
print(polynomial_1)

print('Второй многочлен')
eq_read_2 = Read_file('equation_2.txt')
print(eq_str_2)
polynomial_2 = Create_dict_polynomial(eq_read_2)
print(polynomial_2)

print('Сумма многочленов')
sum_pol = Sum_of_polynomials(polynomial_1, polynomial_2)
print(sum_pol)
str_sum_of_polynomials = Create_string(sum_pol)
print(str_sum_of_polynomials)

Write_file(str_sum_of_polynomials, 'sum_of_polynomials.txt')