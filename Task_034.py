# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# Кодирование длин серий (англ. run-length encoding, RLE) или кодирование повторов — алгоритм сжатия данных, заменяющий повторяющиеся символы (серии) на один символ и число его повторов. 

# запись в файл
def Write_file(str: str, name_file: str):
    data = open(name_file, 'w') # открытие на запись
    data.writelines(str)
    data.close()

# чтение из файла
def Read_file(name_file: str) -> str:
    str = ''
    data = open(name_file, 'r') # открытие на чтение 
    for line in data:
        str += line
    data.close()
    return str

def RLE(my_str) :
    res = ''
    for j in range(len(my_str)-1):
        count = 1
        if my_str[j] == my_str[j+1]:
            count+=1
        else:
            res = res + str(count) + str(my_str[j])

    return res
        

my_str = 'aaaaabbbcccc'

Write_file(my_str,'String.txt')
str_read = Read_file('String.txt')
str_new = RLE(str_read)
print(str_new)