# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

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
    temp = my_str[0]
    count = 0
    for char in my_str:
        if char == temp:
            count+=1
        else:
            res = res + f'{count}{temp}'
            temp = char
            count = 1
    else:
        res = res + f'{count}{temp}'
    return res

def decod(my_str):
    res = ''
    count = 1
    for char in my_str:
        if char.isdigit():
            count = int(char)
        else:
            res = res + count*char
    return res

        
my_str = 'aaaaabbbcccc'

Write_file(my_str,'String.txt')
str_read = Read_file('String.txt')
print(str_read)
str_new = RLE(str_read)
print(str_new)

print(decod(str_new))