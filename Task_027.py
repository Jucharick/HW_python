# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
 
import random

def Create_dict(k: int) -> dict:
    equation = {}
    for i in range(k, -1, -1): # до степени 0 => граница -1 не включается
        equation[i] = random.randint(0, 101)
    return equation


def Create_string(equation: dict) -> str:
    eq_str = ''
    for k, v in equation.items(): # item() возвращает объект представления, который отображает список пары кортежей (ключ, значение) данного словаря
        if k == 1:
            eq_str += f'{v}*x + '
        elif k == 0:
            eq_str += f'{v}'
        elif v == 0:
            eq_str += f''
        else:
            eq_str += f'{v}*x**{k} + '
    else:
        eq_str += f' = 0'
    return eq_str

def Write_file(str: str, name_file: str):
    data = open(name_file, 'w') # открытие на запись
    data.writelines(str)
    data.close()


k_1 = int(input('Введите максимальную степень для многочлена: '))
equation_1 = Create_dict(k_1)
# print(equation_1)
eq_str_1 = Create_string(equation_1)
print(eq_str_1)
Write_file(eq_str_1,'equation_1.txt')

k_2 = int(input('Введите максимальную степень для второго многочлена: '))
equation_2 = Create_dict(k_2)
# print(equation_2)
eq_str_2 = Create_string(equation_2)
print(eq_str_2)
Write_file(eq_str_2, 'equation_2.txt')