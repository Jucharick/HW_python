# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def Read_file(name_file: str) -> str:
    str = ''
    data = open(name_file, 'r') # открытие на чтение 
    for line in data:
        str += line
    data.close()
    return str

def Create_dict_polynomial(new_string: str) -> dict:
    equation = {}
    polynomial = new_string.replace(' ', '').replace('=0', ''). replace('+', ' ').split()
    len_str = len(polynomial) - 1
    for i in range(len_str, -1, -1):
        if polynomial[len_str - i].startswith('x'):
            equation[i] = polynomial[len_str - i]
        else: 
            equation[i] = int(polynomial[len_str - i].split('*')[0])
    return equation

def Sum_of_polynomials(dict_1: dict, dict_2: dict) -> dict:
    sum_pol = {}
    if len(dict_1) > len(dict_2):
        for k, v in dict_1.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
            sum_pol[k] = dict_1.get(k, v) + dict_2.get(k, v)
    if len(dict_1) < len(dict_2):
        for k, v in dict_2.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
            sum_pol[k] = dict_1.get(k, v) + dict_2.get(k, v)
    return sum_pol
        



print('Первый многочлен')
eq_str_1 = Read_file('equation_1.txt')
print(eq_str_1)
polynomial_1 = Create_dict_polynomial(eq_str_1)
print(polynomial_1)

print('Второй многочлен')
eq_str_2 = Read_file('equation_2.txt')
print(eq_str_2)
polynomial_2 = Create_dict_polynomial(eq_str_2)
print(polynomial_2)

print('Сумма многочленов')
sum_pol = Sum_of_polynomials(polynomial_1, polynomial_2)
print(sum_pol)