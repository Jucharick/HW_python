# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def Read_file(name_file: str) -> str:
    str = ''
    data = open(name_file, 'r') # открытие на чтение 
    for line in data:
        str += line
    data.close()
    return str

def Create_dict_equation(str: str) -> dict:
    equation = {}

    return equation







eq_str_1 = Read_file('equation_1.txt')
print(eq_str_1)
equation_1 = Create_dict_equation(eq_str_1)
print(equation_1)




eq_str_2 = Read_file('equation_2.txt')
print(eq_str_2)
equation_2 = Create_dict_equation(eq_str_2)
print(equation_2)